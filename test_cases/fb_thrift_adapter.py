import sys
sys.path.insert(0, './codegen/fb_thrift')

try:
    from thrift.util.Serializer import serialize, deserialize
    from thrift.protocol.TBinaryProtocol import TBinaryProtocolFactory
    factory = TBinaryProtocolFactory()

    import struct_map.ttypes as struct_map_ttypes
    import test.ttypes as test_ttypes

    class FBThriftAdapter(object):
        NAME = 'fb_thrift'

        def encoder_string(self, data):
            return serialize(factory, test_ttypes.Str(data))

        def decoder_string(self, data):
            return deserialize(factory, data, test_ttypes.Str()).data

        def encoder_bytes(self, data):
            return serialize(factory, test_ttypes.Bin(data))

        def decoder_bytes(self, data):
            return deserialize(factory, data, test_ttypes.Bin()).data

        def encoder_integer(self, data):
            return serialize(factory, test_ttypes.Int(data))

        def decoder_integer(self, data):
            return deserialize(factory, data, test_ttypes.Int()).data

        def encoder_float(self, data):
            return serialize(factory, test_ttypes.Float(data))

        def decoder_float(self, data):
            return deserialize(factory, data, test_ttypes.Float()).data

        def encoder_boolean(self, data):
            return serialize(factory, test_ttypes.Bool(data))

        def decoder_boolean(self, data):
            return deserialize(factory, data, test_ttypes.Bool()).data

        def encoder_array(self, data):
            return serialize(factory, test_ttypes.Array(data))

        def decoder_array(self, data):
            return deserialize(factory, data, test_ttypes.Array()).data

        def encoder_map(self, data):
            return serialize(factory, test_ttypes.Map(data))

        def decoder_map(self, data):
            return deserialize(factory, data, test_ttypes.Map()).data

        def encoder_struct_10(self, data):
            return serialize(factory, test_ttypes.Struct10(**data))

        def decoder_struct_10(self, data):
            return deserialize(
                factory,
                data,
                test_ttypes.Struct10(),
            ).__dict__

        def encoder_struct_map(self, data):
            return serialize(
                factory,
                struct_map_ttypes.StructMap(**data),
            )

        def decoder_struct_map(self, data):
            return deserialize(
                factory,
                data,
                struct_map_ttypes.StructMap(),
            ).__dict__

        def encoder_simple_list(self, data):
            return serialize(factory, test_ttypes.SimpleList(data))

        def decoder_simple_list(self, data):
            return deserialize(
                factory,
                data,
                test_ttypes.SimpleList(),
            ).ints

        def encoder_points_list(self, data):
            return serialize(factory, test_ttypes.PointsList(data))

        def decoder_points_list(self, data):
            return deserialize(
                factory,
                data,
                test_ttypes.PointsList(),
            ).points

except ImportError:
    class FBThriftAdapter(object):
        NAME = 'fb_thrift'
