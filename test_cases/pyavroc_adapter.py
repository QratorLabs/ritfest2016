import sys
sys.path.insert(0, './codegen/pyavroc')

import _pyavroc


class PyavrocAdapter(object):
    NAME = 'pyavroc'

    def __init__(self):
        with open('specs/str.avsc', 'r') as f:
            schema = f.read()
            self.str_reader = _pyavroc.AvroDeserializer(schema)
            self.str_writer = _pyavroc.AvroSerializer(schema)

        with open('specs/bin.avsc', 'r') as f:
            schema = f.read()
            self.bin_reader = _pyavroc.AvroDeserializer(schema)
            self.bin_writer = _pyavroc.AvroSerializer(schema)

        with open('specs/int.avsc', 'r') as f:
            schema = f.read()
            self.int_reader = _pyavroc.AvroDeserializer(schema)
            self.int_writer = _pyavroc.AvroSerializer(schema)

        with open('specs/float.avsc', 'r') as f:
            schema = f.read()
            self.float_reader = _pyavroc.AvroDeserializer(schema)
            self.float_writer = _pyavroc.AvroSerializer(schema)

        with open('specs/null.avsc', 'r') as f:
            schema = f.read()
            self.null_reader = _pyavroc.AvroDeserializer(schema)
            self.null_writer = _pyavroc.AvroSerializer(schema)

        with open('specs/bool.avsc', 'r') as f:
            schema = f.read()
            self.bool_reader = _pyavroc.AvroDeserializer(schema)
            self.bool_writer = _pyavroc.AvroSerializer(schema)

        with open('specs/array.avsc', 'r') as f:
            schema = f.read()
            self.array_reader = _pyavroc.AvroDeserializer(schema)
            self.array_writer = _pyavroc.AvroSerializer(schema)

        with open('specs/map.avsc', 'r') as f:
            schema = f.read()
            self.map_reader = _pyavroc.AvroDeserializer(schema)
            self.map_writer = _pyavroc.AvroSerializer(schema)

        with open('specs/struct10.avsc', 'r') as f:
            schema = f.read()
            self.struct10_reader = _pyavroc.AvroDeserializer(schema)
            self.struct10_writer = _pyavroc.AvroSerializer(schema)

        with open('specs/struct_map.avsc', 'r') as f:
            schema = f.read()
            self.struct_map_reader = _pyavroc.AvroDeserializer(schema)
            self.struct_map_writer = _pyavroc.AvroSerializer(schema)

        with open('specs/simple_list.avsc', 'r') as f:
            schema = f.read()
            self.simple_list_reader = _pyavroc.AvroDeserializer(schema)
            self.simple_list_writer = _pyavroc.AvroSerializer(schema)

        with open('specs/points_list.avsc', 'r') as f:
            schema = f.read()
            self.points_list_reader = _pyavroc.AvroDeserializer(schema)
            self.points_list_writer = _pyavroc.AvroSerializer(schema)

    def encoder_string(self, data):
        return self.str_writer.serialize(data)

    def decoder_string(self, data):
        return self.str_reader.deserialize(data)

    def encoder_bytes(self, data):
        return self.bin_writer.serialize(data)

    def decoder_bytes(self, data):
        return self.bin_reader.deserialize(data)

    def encoder_integer(self, data):
        return self.int_writer.serialize(data)

    def decoder_integer(self, data):
        return self.int_reader.deserialize(data)

    def encoder_float(self, data):
        return self.float_writer.serialize(data)

    def decoder_float(self, data):
        return self.float_reader.deserialize(data)

    def encoder_null(self, data):
        return self.null_writer.serialize(data)

    def decoder_null(self, data):
        return self.null_reader.deserialize(data)

    def encoder_boolean(self, data):
        return self.bool_writer.serialize(data)

    def decoder_boolean(self, data):
        return self.bool_reader.deserialize(data)

    def encoder_array(self, data):
        return self.array_writer.serialize(data)

    def decoder_array(self, data):
        return self.array_reader.deserialize(data)

    def encoder_map(self, data):
        return self.map_writer.serialize(data)

    def decoder_map(self, data):
        return self.map_reader.deserialize(data)

    def encoder_struct_10(self, data):
        return self.struct10_writer.serialize(data)

    def decoder_struct_10(self, data):
        return self.struct10_reader.deserialize(data)

    def encoder_struct_map(self, data):
        return self.struct_map_writer.serialize(data)

    def decoder_struct_map(self, data):
        return self.struct_map_reader.deserialize(data)

    def encoder_simple_list(self, data):
        return self.simple_list_writer.serialize(
            data
        )

    def decoder_simple_list(self, data):
        return self.simple_list_reader.deserialize(data)

    def encoder_points_list(self, data):
        return self.points_list_writer.serialize(
            data
        )

    def decoder_points_list(self, data):
        return self.points_list_reader.deserialize(data)
