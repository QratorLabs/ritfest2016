import io
import avro.io
try:
    from avro.schema import parse
except ImportError:
    from avro.schema import Parse as parse


class ApacheAvroAdapter(object):
    NAME = 'avro'

    def __init__(self):
        with open('specs/str.avsc', 'r') as f:
            schema = parse(f.read())
            self.str_reader = avro.io.DatumReader(schema)
            self.str_writer = avro.io.DatumWriter(schema)

        with open('specs/bin.avsc', 'r') as f:
            schema = parse(f.read())
            self.bin_reader = avro.io.DatumReader(schema)
            self.bin_writer = avro.io.DatumWriter(schema)

        with open('specs/int.avsc', 'r') as f:
            schema = parse(f.read())
            self.int_reader = avro.io.DatumReader(schema)
            self.int_writer = avro.io.DatumWriter(schema)

        with open('specs/float.avsc', 'r') as f:
            schema = parse(f.read())
            self.float_reader = avro.io.DatumReader(schema)
            self.float_writer = avro.io.DatumWriter(schema)

        with open('specs/null.avsc', 'r') as f:
            schema = parse(f.read())
            self.null_reader = avro.io.DatumReader(schema)
            self.null_writer = avro.io.DatumWriter(schema)

        with open('specs/bool.avsc', 'r') as f:
            schema = parse(f.read())
            self.bool_reader = avro.io.DatumReader(schema)
            self.bool_writer = avro.io.DatumWriter(schema)

        with open('specs/array.avsc', 'r') as f:
            schema = parse(f.read())
            self.array_reader = avro.io.DatumReader(schema)
            self.array_writer = avro.io.DatumWriter(schema)

        with open('specs/map.avsc', 'r') as f:
            schema = parse(f.read())
            self.map_reader = avro.io.DatumReader(schema)
            self.map_writer = avro.io.DatumWriter(schema)

        with open('specs/struct10.avsc', 'r') as f:
            schema = parse(f.read())
            self.struct10_reader = avro.io.DatumReader(schema)
            self.struct10_writer = avro.io.DatumWriter(schema)

        with open('specs/struct_map.avsc', 'r') as f:
            schema = parse(f.read())
            self.struct_map_reader = avro.io.DatumReader(schema)
            self.struct_map_writer = avro.io.DatumWriter(schema)

        with open('specs/simple_list.avsc', 'r') as f:
            schema = parse(f.read())
            self.simple_list_reader = avro.io.DatumReader(schema)
            self.simple_list_writer = avro.io.DatumWriter(schema)

        with open('specs/points_list.avsc', 'r') as f:
            schema = parse(f.read())
            self.points_list_reader = avro.io.DatumReader(schema)
            self.points_list_writer = avro.io.DatumWriter(schema)

    def encoder_string(self, data):
        io_stream = io.BytesIO()
        self.str_writer.write(
            data,
            avro.io.BinaryEncoder(io_stream),
        )
        return io_stream.getvalue()

    def decoder_string(self, data):
        io_stream = io.BytesIO(data)
        return self.str_reader.read(avro.io.BinaryDecoder(io_stream))

    def encoder_bytes(self, data):
        io_stream = io.BytesIO()
        self.bin_writer.write(
            data,
            avro.io.BinaryEncoder(io_stream),
        )
        return io_stream.getvalue()

    def decoder_bytes(self, data):
        io_stream = io.BytesIO(data)
        return self.bin_reader.read(avro.io.BinaryDecoder(io_stream))

    def encoder_integer(self, data):
        io_stream = io.BytesIO()
        self.int_writer.write(
            data,
            avro.io.BinaryEncoder(io_stream),
        )
        return io_stream.getvalue()

    def decoder_integer(self, data):
        io_stream = io.BytesIO(data)
        return self.int_reader.read(avro.io.BinaryDecoder(io_stream))

    def encoder_float(self, data):
        io_stream = io.BytesIO()
        self.float_writer.write(
            data,
            avro.io.BinaryEncoder(io_stream),
        )
        return io_stream.getvalue()

    def decoder_float(self, data):
        io_stream = io.BytesIO(data)
        return self.float_reader.read(avro.io.BinaryDecoder(io_stream))

    def encoder_null(self, data):
        io_stream = io.BytesIO()
        self.null_writer.write(
            data,
            avro.io.BinaryEncoder(io_stream),
        )
        return io_stream.getvalue()

    def decoder_null(self, data):
        io_stream = io.BytesIO(data)
        return self.null_reader.read(avro.io.BinaryDecoder(io_stream))

    def encoder_boolean(self, data):
        io_stream = io.BytesIO()
        self.bool_writer.write(
            data,
            avro.io.BinaryEncoder(io_stream),
        )
        return io_stream.getvalue()

    def decoder_boolean(self, data):
        io_stream = io.BytesIO(data)
        return self.bool_reader.read(avro.io.BinaryDecoder(io_stream))

    def encoder_array(self, data):
        io_stream = io.BytesIO()
        self.array_writer.write(
            data,
            avro.io.BinaryEncoder(io_stream),
        )
        return io_stream.getvalue()

    def decoder_array(self, data):
        io_stream = io.BytesIO(data)
        return self.array_reader.read(avro.io.BinaryDecoder(io_stream))

    def encoder_map(self, data):
        io_stream = io.BytesIO()
        self.map_writer.write(
            data,
            avro.io.BinaryEncoder(io_stream),
        )
        return io_stream.getvalue()

    def decoder_map(self, data):
        io_stream = io.BytesIO(data)
        return self.map_reader.read(avro.io.BinaryDecoder(io_stream))

    def encoder_struct_10(self, data):
        io_stream = io.BytesIO()
        self.struct10_writer.write(
            data,
            avro.io.BinaryEncoder(io_stream),
        )
        return io_stream.getvalue()

    def decoder_struct_10(self, data):
        io_stream = io.BytesIO(data)
        return self.struct10_reader.read(avro.io.BinaryDecoder(io_stream))

    def encoder_struct_map(self, data):
        io_stream = io.BytesIO()
        self.struct_map_writer.write(
            data,
            avro.io.BinaryEncoder(io_stream),
        )
        return io_stream.getvalue()

    def decoder_struct_map(self, data):
        io_stream = io.BytesIO(data)
        return self.struct_map_reader.read(avro.io.BinaryDecoder(io_stream))

    def encoder_simple_list(self, data):
        io_stream = io.BytesIO()

        self.simple_list_writer.write(
            data,
            avro.io.BinaryEncoder(io_stream),
        )
        return io_stream.getvalue()

    def decoder_simple_list(self, data):
        io_stream = io.BytesIO(data)
        return self.simple_list_reader.read(
            avro.io.BinaryDecoder(io_stream),
        )

    def encoder_points_list(self, data):
        io_stream = io.BytesIO()

        self.points_list_writer.write(
            data,
            avro.io.BinaryEncoder(io_stream),
        )
        return io_stream.getvalue()

    def decoder_points_list(self, data):
        io_stream = io.BytesIO(data)
        return self.points_list_reader.read(
            avro.io.BinaryDecoder(io_stream),
        )
