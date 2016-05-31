import sys
sys.path.insert(0, './codegen')

try:
    import protobuf3_gen.struct_map as struct_map_pb2
    import protobuf3_gen.test as test_pb2

    class Protobuf3Adapter(object):
        NAME = 'protobuf3'

        def encoder_string(self, data):
            obj = test_pb2.Str()
            obj.data = data
            return obj.encode_to_bytes()

        def decoder_string(self, data):
            obj = test_pb2.Str()
            obj.parse_from_bytes(data)
            return obj.data

        def encoder_bytes(self, data):
            obj = test_pb2.Bin()
            obj.data = data
            return obj.encode_to_bytes()

        def decoder_bytes(self, data):
            obj = test_pb2.Bin()
            obj.parse_from_bytes(data)
            return obj.data

        def encoder_integer(self, data):
            obj = test_pb2.Int()
            obj.data = data
            return obj.encode_to_bytes()

        def decoder_integer(self, data):
            obj = test_pb2.Int()
            obj.parse_from_bytes(data)
            return obj.data

        def encoder_float(self, data):
            obj = test_pb2.Float()
            obj.data = data
            return obj.encode_to_bytes()

        def decoder_float(self, data):
            obj = test_pb2.Float()
            obj.parse_from_bytes(data)
            return obj.data

        def encoder_boolean(self, data):
            obj = test_pb2.Bool()
            obj.data = data
            return obj.encode_to_bytes()

        def decoder_boolean(self, data):
            obj = test_pb2.Bool()
            obj.parse_from_bytes(data)
            return obj.data

        def encoder_array(self, data):
            obj = test_pb2.Array()
            obj.data.extend(data)
            return obj.encode_to_bytes()

        def decoder_array(self, data):
            obj = test_pb2.Array()
            obj.parse_from_bytes(data)
            return list(obj.data)

        def encoder_map(self, data):
            obj = test_pb2.Map()

            for key, value in data.items():
                entry = test_pb2.MapEntry()
                entry.key = key
                entry.value = value
                obj.data.append(entry)

            return obj.encode_to_bytes()

        def decoder_map(self, data):
            obj = test_pb2.Map()
            obj.parse_from_bytes(data)
            return {
                entry.key: entry.value
                for entry in obj.data
            }

        def encoder_struct_10(self, data):
            obj = test_pb2.Struct10()

            for k, v in data.items():
                setattr(obj, k, v)

            return obj.encode_to_bytes()

        def decoder_struct_10(self, data):
            obj = test_pb2.Struct10()
            obj.parse_from_bytes(data)
            return {
                v.field_name: getattr(obj, v.field_name)
                for v in obj._Message__fields.values()
            }

        def encoder_struct_map(self, data):
            obj = struct_map_pb2.StructMap()

            for k, v in data.items():
                setattr(obj, k, v)

            return obj.encode_to_bytes()

        def decoder_struct_map(self, data):
            obj = struct_map_pb2.StructMap()
            obj.parse_from_bytes(data)
            return {
                v.field_name: getattr(obj, v.field_name)
                for v in obj._Message__fields.values()
            }

        def encoder_simple_list(self, data):
            obj = test_pb2.SimpleList()
            obj.ints.extend(data)
            return obj.encode_to_bytes()

        def decoder_simple_list(self, data):
            obj = test_pb2.SimpleList()
            obj.parse_from_bytes(data)
            return list(obj.ints)

        def encoder_points_list(self, data):
            obj = test_pb2.PointsList()
            for p in data:
                po = test_pb2.Point()
                po.x, po.y = p
                obj.points.append(po)

            return obj.encode_to_bytes()

        def decoder_points_list(self, data):
            obj = test_pb2.PointsList()
            obj.parse_from_bytes(data)
            return [[p.x, p.y] for p in obj.points]

except ImportError:
    class Protobuf3Adapter(object):
        NAME = 'protobuf3'
