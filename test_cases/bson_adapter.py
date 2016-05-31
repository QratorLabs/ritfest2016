import bson


class BsonAdapter(object):
    NAME = 'bson'

    def encoder_string(self, data):
        return bson.dumps({'': data})

    def decoder_string(self, data):
        return bson.loads(data)['']

    encoder_bytes = encoder_string
    decoder_bytes = decoder_string

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

    def encoder_map(self, data):
        return bson.dumps(data)

    def decoder_map(self, data):
        return bson.loads(data)

    encoder_struct_map = encoder_string
    decoder_struct_map = decoder_string

    encoder_simple_list = encoder_string
    decoder_simple_list = decoder_string

    encoder_points_list = encoder_string
    decoder_points_list = decoder_string
