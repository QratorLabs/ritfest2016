#!/usr/bin/env python2

import csv
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


class MeasureSize(object):
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

    def __init__(self):
        self.data = {
            'string': {
                '0': u'',
                'ascii10': u' ' * 10,
                'ascii1000': u' ' * 1000,
                'uni10': b'\xd1\x8f'.decode('utf8') * 10,
                'uni1000': b'\xd1\x8f'.decode('utf8') * 1000,
            },
            'bytes': {
                '0': b'',
                '10': b' ' * 10,
                '1000': b' ' * 1000,
            },
            'integer': {
                '0': 0,
                '1byte': 100,
                '2byte': 1000,
                '4byte': 1000000000,
            },
            'float': {
                '0': 0.0,
                '2.5': 2.5,
                '1/3': 1.0/3.0,
                '1000000000/3': 1000000000.0/3.0,
            },
            'null': {
                'null': None,
            },
            'boolean': {
                'true': True,
            },
            'array': {
                'empty': [],
                'one_empty_string': [u''],
                '1000_empty_string': [u''] * 1000,
            },
            'map': {
                'empty': {},
                'empty_string:empty_string': {u'': u''},
                'ascii10:empty_string': {
                    u'f' + str(i).rjust(9, '0'): u''
                    for i in range(10)
                },
            },
            'struct_10': {
                'ascii10:empty_string': {
                    u'f' + str(i).rjust(9, '0'): u''
                    for i in range(10)
                },
            },
        }

        self.adapters = {
            adapter.NAME: adapter
            for adapter in self.ADAPTERS
        }

    def measure(self, module_class_name, test_type, test_name):
        module = self.adapters[module_class_name]()
        encoder = getattr(module, 'encoder_' + test_type, None)
        decoder = getattr(module, 'decoder_' + test_type, None)

        if not encoder or not decoder:
            return 'Unsupported'

        test_data = self.data[test_type][test_name]
        try:
            serialized = encoder(test_data)
            decoded = decoder(serialized)
        except (TypeError, ValueError, AssertionError):
            return 'Coding error'

        if type(decoded) != type(test_data):
            return 'Type mismatch {} to {}'.format(
                type(test_data),
                type(decoded),
            )

        if decoded != test_data:
            return 'Value mismatch'

        return len(serialized)

    def measure_all(self):
        headers = ['module']
        for test_type in sorted(self.data):
            for test_name in sorted(self.data[test_type]):
                headers.append('{}_{}'.format(test_type, test_name))
        yield headers

        for module_class in self.ADAPTERS:
            sizes = []
            for test_type in sorted(self.data):
                for test_name in sorted(self.data[test_type]):
                    sizes.append(
                        self.measure(module_class.NAME, test_type, test_name)
                    )
            yield [module_class.NAME] + sizes


measure = MeasureSize()
writer = csv.writer(sys.stdout)
writer.writerows(measure.measure_all())
