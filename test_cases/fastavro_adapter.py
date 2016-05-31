import fastavro
import io
import json


class FastAvroAdapter(object):
    NAME = 'fastavro'

    def __init__(self):
        with open('specs/str.avsc', 'r') as f:
            self.str_schema = json.loads(f.read())

        with open('specs/bin.avsc', 'r') as f:
            self.bin_schema = json.loads(f.read())

        with open('specs/int.avsc', 'r') as f:
            self.int_schema = json.loads(f.read())

        with open('specs/float.avsc', 'r') as f:
            self.float_schema = json.loads(f.read())

        with open('specs/null.avsc', 'r') as f:
            self.null_schema = json.loads(f.read())

        with open('specs/bool.avsc', 'r') as f:
            self.bool_schema = json.loads(f.read())

        with open('specs/array.avsc', 'r') as f:
            self.array_schema = json.loads(f.read())

        with open('specs/map.avsc', 'r') as f:
            self.map_schema = json.loads(f.read())

        with open('specs/struct10.avsc', 'r') as f:
            self.struct10_schema = json.loads(f.read())

        with open('specs/struct_map.avsc', 'r') as f:
            self.struct_map_schema = json.loads(f.read())

        with open('specs/simple_list.avsc', 'r') as f:
            self.simple_list_dict_schema = json.loads(f.read())

        with open('specs/points_list.avsc', 'r') as f:
            self.points_list_dict_schema = json.loads(f.read())

    def encoder_string(self, data):
        io_stream = io.BytesIO()
        fastavro.schemaless_writer(io_stream, self.str_schema, data)
        return io_stream.getvalue()

    def decoder_string(self, data):
        io_stream = io.BytesIO(data)
        return fastavro.schemaless_reader(io_stream, self.str_schema)

    def encoder_bytes(self, data):
        io_stream = io.BytesIO()
        fastavro.schemaless_writer(io_stream, self.bin_schema, data)
        return io_stream.getvalue()

    def decoder_bytes(self, data):
        io_stream = io.BytesIO(data)
        return fastavro.schemaless_reader(io_stream, self.bin_schema)

    def encoder_integer(self, data):
        io_stream = io.BytesIO()
        fastavro.schemaless_writer(io_stream, self.int_schema, data)
        return io_stream.getvalue()

    def decoder_integer(self, data):
        io_stream = io.BytesIO(data)
        return fastavro.schemaless_reader(io_stream, self.int_schema)

    def encoder_float(self, data):
        io_stream = io.BytesIO()
        fastavro.schemaless_writer(io_stream, self.float_schema, data)
        return io_stream.getvalue()

    def decoder_float(self, data):
        io_stream = io.BytesIO(data)
        return fastavro.schemaless_reader(io_stream, self.float_schema)

    def encoder_null(self, data):
        io_stream = io.BytesIO()
        fastavro.schemaless_writer(io_stream, self.null_schema, data)
        return io_stream.getvalue()

    def decoder_null(self, data):
        io_stream = io.BytesIO(data)
        return fastavro.schemaless_reader(io_stream, self.null_schema)

    def encoder_boolean(self, data):
        io_stream = io.BytesIO()
        fastavro.schemaless_writer(io_stream, self.bool_schema, data)
        return io_stream.getvalue()

    def decoder_boolean(self, data):
        io_stream = io.BytesIO(data)
        return fastavro.schemaless_reader(io_stream, self.bool_schema)

    def encoder_array(self, data):
        io_stream = io.BytesIO()
        fastavro.schemaless_writer(io_stream, self.array_schema, data)
        return io_stream.getvalue()

    def decoder_array(self, data):
        io_stream = io.BytesIO(data)
        return fastavro.schemaless_reader(io_stream, self.array_schema)

    def encoder_map(self, data):
        io_stream = io.BytesIO()
        fastavro.schemaless_writer(io_stream, self.map_schema, data)
        return io_stream.getvalue()

    def decoder_map(self, data):
        io_stream = io.BytesIO(data)
        return fastavro.schemaless_reader(io_stream, self.map_schema)

    def encoder_struct_10(self, data):
        io_stream = io.BytesIO()
        fastavro.schemaless_writer(io_stream, self.struct10_schema, data)
        return io_stream.getvalue()

    def decoder_struct_10(self, data):
        io_stream = io.BytesIO(data)
        return fastavro.schemaless_reader(io_stream, self.struct10_schema)

    def encoder_struct_map(self, data):
        io_stream = io.BytesIO()
        fastavro.schemaless_writer(
            io_stream,
            self.struct_map_schema,
            data,
        )
        return io_stream.getvalue()

    def decoder_struct_map(self, data):
        io_stream = io.BytesIO(data)
        return fastavro.schemaless_reader(io_stream, self.struct_map_schema)

    def encoder_simple_list(self, data):
        io_stream = io.BytesIO()
        fastavro.schemaless_writer(
            io_stream,
            self.simple_list_dict_schema,
            data,
        )
        return io_stream.getvalue()

    def decoder_simple_list(self, data):
        io_stream = io.BytesIO(data)
        return fastavro.schemaless_reader(
            io_stream,
            self.simple_list_dict_schema,
        )

    def encoder_points_list(self, data):
        io_stream = io.BytesIO()
        fastavro.schemaless_writer(
            io_stream,
            self.points_list_dict_schema,
            data,
        )
        return io_stream.getvalue()

    def decoder_points_list(self, data):
        io_stream = io.BytesIO(data)
        return fastavro.schemaless_reader(
            io_stream,
            self.points_list_dict_schema,
        )
