#!/usr/bin/env python2

import csv
import gc
import math
import pickle
import sys

from test_cases.apache_avro_adapter import ApacheAvroAdapter
from test_cases.apache_thrift_adapter import ApacheThriftAdapter
from test_cases.bson_adapter import BsonAdapter
from test_cases.cprotobuf_adapter import CProtobufAdapter
from test_cases.fastavro_adapter import FastAvroAdapter
from test_cases.fb_thrift_adapter import FBThriftAdapter
from test_cases.google_proto_adapter import GoogleProtoAdapter
from test_cases.json_adapter import JsonAdapter
from test_cases.msgpack_adapter import MsgpackAdapter
from test_cases.pickle_adapter import PickleAdapter
from test_cases.protobuf3_adapter import Protobuf3Adapter
from test_cases.pyavroc_adapter import PyavrocAdapter
from test_cases.thriftpy_adapter import ThriftPyAdapter
from test_cases.thriftrw_adapter import ThriftRwAdapter
from test_cases.ujson_adapter import UJsonAdapter


try:
    import time
    monotonic_time = time.monotonic
except AttributeError:
    import monotonic
    monotonic_time = monotonic.monotonic


class Measure(object):
    ADAPTERS = [
        PickleAdapter,
        JsonAdapter,
        UJsonAdapter,
        BsonAdapter,
        MsgpackAdapter,

        GoogleProtoAdapter,
        CProtobufAdapter,
        Protobuf3Adapter,

        ApacheThriftAdapter,
        FBThriftAdapter,
        ThriftPyAdapter,
        ThriftRwAdapter,

        ApacheAvroAdapter,
        FastAvroAdapter,
        PyavrocAdapter,
    ]

    COUNT = 30
    CYCLES = 10

    def __init__(self):
        with open('test_data.bin', 'rb') as f:
            pickled = f.read()
            self.data = pickle.loads(pickled)

        self.data['bytes'] = {
            '': pickled[:len(self.data['string'][''])],
        }

        self.adapters = {
            adapter.NAME: adapter
            for adapter in self.ADAPTERS
        }

    def mean(self, data):
        return sum(data) / len(data)

    def stdev(self, data):
        n = len(data)
        mean = self.mean(data)
        ss = sum((i - mean)**2 for i in data)
        variance = ss / (n - 1)
        return math.sqrt(variance)

    def filter_errors(self, data):
        mean = self.mean(data)
        stdev = self.stdev(data)
        return [i for i in data if abs(i - mean) < stdev]

    def run_measure_retry(self, func, arg):
        count = self.COUNT

        while True:
            count += int(self.COUNT * 0.3)

            times = []
            gc.disable()
            for _ in range(count):
                start_time = monotonic_time()
                for _ in range(self.CYCLES):
                    result = func(arg)
                times.append(monotonic_time() - start_time)
            gc.enable()

            filtered = self.filter_errors(times)
            if len(filtered) >= self.COUNT:
                return result, filtered

            sys.stderr.write('Retry {} {}\n'.format(count, len(filtered)))

    def measure(self, module_class_name, test_type, test_name):
        sys.stderr.write('Run {} {}\n'.format(module_class_name, test_type))

        module = self.adapters[module_class_name]()
        encoder = getattr(module, 'encoder_' + test_type, None)
        decoder = getattr(module, 'decoder_' + test_type, None)

        if not encoder or not decoder:
            return (
                'py{}.{}'.format(
                    sys.version_info.major,
                    sys.version_info.minor,
                ),
                module.NAME,
                '{}_{}'.format(test_type, test_name),
                'Unsupported',
            )

        flags = []
        test_data = self.data[test_type][test_name]

        serialized = encoder(test_data)
        serialized_len = len(serialized)
        decoded = decoder(serialized)

        if type(decoded) != type(test_data):
            flags.append('Type mismatch')

        if decoded != test_data:
            flags.append('Value mismatch')

        _, encode_times = self.run_measure_retry(encoder, test_data)
        _, decode_times = self.run_measure_retry(decoder, serialized)

        return (
            'py{}.{}'.format(sys.version_info.major, sys.version_info.minor),
            module.NAME,
            '{}_{}'.format(test_type, test_name),
            ', '.join(flags),
            serialized_len,

            self.mean(encode_times),
            self.mean(decode_times),
        )

    def measure_all(self):
        for module_class in self.ADAPTERS:
            for test_type in sorted(self.data):
                for test_name in sorted(self.data[test_type]):
                    yield self.measure(module_class.NAME, test_type, test_name)


measure = Measure()
writer = csv.writer(sys.stdout)
writer.writerows(measure.measure_all())
