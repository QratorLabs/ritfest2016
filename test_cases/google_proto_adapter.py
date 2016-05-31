import sys
sys.path.insert(0, './codegen/google_proto')

import struct_map_pb2
import test_pb2


class GoogleProtoAdapter(object):
    NAME = 'google_proto'

    def encoder_string(self, data):
        return test_pb2.Str(data=data).SerializeToString()

    def decoder_string(self, data):
        obj = test_pb2.Str()
        obj.ParseFromString(data)
        return obj.data

    def encoder_bytes(self, data):
        return test_pb2.Bin(data=data).SerializeToString()

    def decoder_bytes(self, data):
        obj = test_pb2.Bin()
        obj.ParseFromString(data)
        return obj.data

    def encoder_integer(self, data):
        return test_pb2.Int(data=data).SerializeToString()

    def decoder_integer(self, data):
        obj = test_pb2.Int()
        obj.ParseFromString(data)
        return obj.data

    def encoder_float(self, data):
        return test_pb2.Float(data=data).SerializeToString()

    def decoder_float(self, data):
        obj = test_pb2.Float()
        obj.ParseFromString(data)
        return obj.data

    def encoder_boolean(self, data):
        return test_pb2.Bool(data=data).SerializeToString()

    def decoder_boolean(self, data):
        obj = test_pb2.Bool()
        obj.ParseFromString(data)
        return obj.data

    def encoder_array(self, data):
        return test_pb2.Array(data=data).SerializeToString()

    def decoder_array(self, data):
        obj = test_pb2.Array()
        obj.ParseFromString(data)
        return list(obj.data)

    def encoder_map(self, data):
        return test_pb2.Map(
            data=[
                test_pb2.MapEntry(key=key, value=value)
                for key, value in data.items()
            ]
        ).SerializeToString()

    def decoder_map(self, data):
        obj = test_pb2.Map()
        obj.ParseFromString(data)
        return {
            entry.key: entry.value
            for entry in obj.data
        }

    def encoder_struct_10(self, data):
        return test_pb2.Struct10(**data).SerializeToString()

    def decoder_struct_10(self, data):
        obj = test_pb2.Struct10()
        obj.ParseFromString(data)
        return {
            k.name: v
            for k, v in obj._fields.items()
        }

    def encoder_struct_map(self, data):
        return struct_map_pb2.StructMap(**data).SerializeToString()

    def decoder_struct_map(self, data):
        obj = struct_map_pb2.StructMap()
        obj.ParseFromString(data)
        return {
            k.name: v
            for k, v in obj._fields.items()
        }

    def encoder_simple_list(self, data):
        return test_pb2.SimpleList(ints=data).SerializeToString()

    def decoder_simple_list(self, data):
        obj = test_pb2.SimpleList()
        obj.ParseFromString(data)
        return list(obj.ints)

    def encoder_points_list(self, data):
        return test_pb2.PointsList(points=[
            test_pb2.Point(x=p[0], y=p[1])
            for p in data
        ]).SerializeToString()

    def decoder_points_list(self, data):
        obj = test_pb2.PointsList()
        obj.ParseFromString(data)
        return [[p.x, p.y] for p in obj.points]
