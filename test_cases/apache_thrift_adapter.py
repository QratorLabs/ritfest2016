import sys
sys.path.insert(0, './codegen/apache_thrift')

try:
    from thrift.TSerialization import serialize, deserialize

    import struct_map.ttypes as struct_map_ttypes
    import test.ttypes as test_ttypes

    class ApacheThriftAdapter(object):
        NAME = 'apache_thrift'

        def encoder_string(self, data):
            return serialize(test_ttypes.Str(data))

        def decoder_string(self, data):
            return deserialize(test_ttypes.Str(), data).data

        def encoder_bytes(self, data):
            return serialize(test_ttypes.Bin(data))

        def decoder_bytes(self, data):
            return deserialize(test_ttypes.Bin(), data).data

        def encoder_integer(self, data):
            return serialize(test_ttypes.Int(data))

        def decoder_integer(self, data):
            return deserialize(test_ttypes.Int(), data).data

        def encoder_float(self, data):
            return serialize(test_ttypes.Float(data))

        def decoder_float(self, data):
            return deserialize(test_ttypes.Float(), data).data

        def encoder_boolean(self, data):
            return serialize(test_ttypes.Bool(data))

        def decoder_boolean(self, data):
            return deserialize(test_ttypes.Bool(), data).data

        def encoder_array(self, data):
            return serialize(test_ttypes.Array(data))

        def decoder_array(self, data):
            return deserialize(test_ttypes.Array(), data).data

        def encoder_map(self, data):
            return serialize(test_ttypes.Map(data))

        def decoder_map(self, data):
            return deserialize(test_ttypes.Map(), data).data

        def encoder_struct_10(self, data):
            return serialize(test_ttypes.Struct10(**data))

        def decoder_struct_10(self, data):
            return deserialize(
                test_ttypes.Struct10(),
                data,
            ).__dict__

        def encoder_struct_map(self, data):
            return serialize(struct_map_ttypes.StructMap(**data))

        def decoder_struct_map(self, data):
            return deserialize(
                struct_map_ttypes.StructMap(),
                data,
            ).__dict__

        def encoder_simple_list(self, data):
            return serialize(test_ttypes.SimpleList(data))

        def decoder_simple_list(self, data):
            return deserialize(
                test_ttypes.SimpleList(),
                data,
            ).ints

        def encoder_points_list(self, data):
            return serialize(test_ttypes.PointsList(data))

        def decoder_points_list(self, data):
            return deserialize(
                test_ttypes.PointsList(),
                data,
            ).points

except ImportError:
    class ApacheThriftAdapter(object):
        NAME = 'apache_thrift'
