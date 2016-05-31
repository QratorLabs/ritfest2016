import sys
import thriftpy._compat

thriftpy._compat.CYTHON = '--no-cython' not in sys.argv[1:]

import thriftpy
import thriftpy.utils


class ThriftPyAdapter(object):
    NAME = 'thriftpy'

    def __init__(self):
        if thriftpy._compat.CYTHON:
            self.NAME += '+cython'

        self.module = thriftpy.load(
            'specs/test.thrift',
            include_dirs=['specs'],
        )

    def encoder_string(self, data):
        return thriftpy.utils.serialize(self.module.Str(data))

    def decoder_string(self, data):
        return thriftpy.utils.deserialize(self.module.Str(), data).data

    def encoder_bytes(self, data):
        return thriftpy.utils.serialize(self.module.Bin(data))

    def decoder_bytes(self, data):
        return thriftpy.utils.deserialize(self.module.Bin(), data).data

    def encoder_integer(self, data):
        return thriftpy.utils.serialize(self.module.Int(data))

    def decoder_integer(self, data):
        return thriftpy.utils.deserialize(self.module.Int(), data).data

    def encoder_float(self, data):
        return thriftpy.utils.serialize(self.module.Float(data))

    def decoder_float(self, data):
        return thriftpy.utils.deserialize(self.module.Float(), data).data

    def encoder_boolean(self, data):
        return thriftpy.utils.serialize(self.module.Bool(data))

    def decoder_boolean(self, data):
        return thriftpy.utils.deserialize(self.module.Bool(), data).data

    def encoder_array(self, data):
        return thriftpy.utils.serialize(self.module.Array(data))

    def decoder_array(self, data):
        return thriftpy.utils.deserialize(self.module.Array(), data).data

    def encoder_map(self, data):
        return thriftpy.utils.serialize(self.module.Map(data))

    def decoder_map(self, data):
        return thriftpy.utils.deserialize(self.module.Map(), data).data

    def encoder_struct_10(self, data):
        return thriftpy.utils.serialize(self.module.Struct10(**data))

    def decoder_struct_10(self, data):
        return thriftpy.utils.deserialize(
            self.module.Struct10(),
            data,
        ).__dict__

    def encoder_struct_map(self, data):
        return thriftpy.utils.serialize(
            self.module.struct_map.StructMap(**data)
        )

    def decoder_struct_map(self, data):
        return thriftpy.utils.deserialize(
            self.module.struct_map.StructMap(),
            data,
        ).__dict__

    def encoder_simple_list(self, data):
        return thriftpy.utils.serialize(self.module.SimpleList(
            data
        ))

    def decoder_simple_list(self, data):
        return thriftpy.utils.deserialize(
            self.module.SimpleList(),
            data,
        ).ints

    def encoder_points_list(self, data):
        return thriftpy.utils.serialize(self.module.PointsList(
            data
        ))

    def decoder_points_list(self, data):
        return thriftpy.utils.deserialize(
            self.module.PointsList(),
            data,
        ).points
