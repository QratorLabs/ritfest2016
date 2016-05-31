#!/usr/bin/env python3

import itertools
import json
import pickle
import string
import random


data_simple_list = [
    random.randint(0, 1000000)
    for _ in range(6000)
]

data_points_list = [
    [random.randint(0, 1000000), random.randint(0, 1000000)]
    for _ in range(6000)
]

data_map = {
    '_'.join(key): ''.join(
        random.choice(string.ascii_letters)
        for _ in range(128)
    )
    for key in itertools.permutations(
        ['long', 'key', 'name', 'foo', 'bar'],
        4,
    )
}

data_string = ''.join(
    random.choice(string.ascii_letters)
    for _ in range(1024 * 1024)
)

data_bytes = pickle.dumps(
    dict(
        string={'': data_string},
        map={'': data_map},
        struct_map={'': data_map},
        simple_list={'': data_simple_list},
        points_list={'': data_points_list},
    ),
    protocol=2,
)

with open('test_data.bin', 'wb') as f:
    f.write(data_bytes)

with open('specs/struct_map.thrift', 'w') as f:
    f.write('struct StructMap {\n')
    for i, key in enumerate(data_map):
        f.write('    {}: required string {},\n'.format(i + 1, key))
    f.write('}\n')

with open('specs/struct_map.proto', 'w') as f:
    f.write('message StructMap {\n')
    for i, key in enumerate(data_map):
        f.write('    required string {} = {};\n'.format(key, i + 1))
    f.write('}\n')

with open('specs/struct_map.avsc', 'w') as f:
    f.write(json.dumps(
        dict(
            namespace="test.avro",
            type="record",
            name="StructMap",
            fields=[
                dict(type='string', name=field)
                for field in data_map
            ]
        ),
        indent=4,
    ))
