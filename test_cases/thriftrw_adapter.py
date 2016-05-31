import thriftrw


class ThriftRwAdapter(object):
    NAME = 'thriftrw'

    def __init__(self):
        self.module = thriftrw.load(
            'specs/test.thrift',
        )

    def encoder_string(self, data):
        return self.module.dumps(self.module.Str(data))

    def decoder_string(self, data):
        return self.module.loads(self.module.Str, data).data

    def encoder_bytes(self, data):
        return self.module.dumps(self.module.Bin(data))

    def decoder_bytes(self, data):
        return self.module.loads(self.module.Bin, data).data

    def encoder_integer(self, data):
        return self.module.dumps(self.module.Int(data))

    def decoder_integer(self, data):
        return self.module.loads(self.module.Int, data).data

    def encoder_float(self, data):
        return self.module.dumps(self.module.Float(data))

    def decoder_float(self, data):
        return self.module.loads(self.module.Float, data).data

    def encoder_boolean(self, data):
        return self.module.dumps(self.module.Bool(data))

    def decoder_boolean(self, data):
        return self.module.loads(self.module.Bool, data).data

    def encoder_array(self, data):
        return self.module.dumps(self.module.Array(data))

    def decoder_array(self, data):
        return self.module.loads(self.module.Array, data).data

    def encoder_map(self, data):
        return self.module.dumps(self.module.Map(data))

    def decoder_map(self, data):
        return self.module.loads(self.module.Map, data).data

    def encoder_struct_10(self, data):
        return self.module.dumps(self.module.Struct10(**data))

    def decoder_struct_10(self, data):
        data = self.module.loads(self.module.Struct10, data)
        return {
            f.name: getattr(data, f.name)
            for f in data.type_spec.fields
        }

    def encoder_struct_map(self, data):
        return self.module.dumps(self.module.struct_map.StructMap(**data))

    def decoder_struct_map(self, data):
        data = self.module.loads(self.module.struct_map.StructMap, data)
        return {
            f.name: getattr(data, f.name)
            for f in data.type_spec.fields
        }

    def encoder_simple_list(self, data):
        return self.module.dumps(self.module.SimpleList(data))

    def decoder_simple_list(self, data):
        return self.module.loads(
            self.module.SimpleList,
            data,
        ).ints

    def encoder_points_list(self, data):
        return self.module.dumps(self.module.PointsList(data))

    def decoder_points_list(self, data):
        return self.module.loads(
            self.module.PointsList,
            data,
        ).points
