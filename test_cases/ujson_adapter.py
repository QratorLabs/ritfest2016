import base64
import ujson


class UJsonAdapter(object):
    NAME = 'ujson'

    def encoder_string(self, data):
        return ujson.dumps(data)

    def decoder_string(self, data):
        return ujson.loads(data)

    def encoder_bytes(self, data):
        return ujson.dumps(base64.encodestring(data).decode())

    def decoder_bytes(self, data):
        return base64.decodestring(ujson.loads(data).encode())

    encoder_integer = encoder_string
    decoder_integer = decoder_string

    encoder_float = encoder_string
    decoder_float = decoder_string

    encoder_null = encoder_string
    decoder_null = decoder_string

    encoder_boolean = encoder_string
    decoder_boolean = decoder_string

    encoder_array = encoder_string
    decoder_array = decoder_string

    encoder_map = encoder_string
    decoder_map = decoder_string

    encoder_struct_map = encoder_string
    decoder_struct_map = decoder_string

    encoder_simple_list = encoder_string
    decoder_simple_list = decoder_string

    encoder_points_list = encoder_string
    decoder_points_list = decoder_string
