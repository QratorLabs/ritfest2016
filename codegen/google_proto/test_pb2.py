# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import struct_map_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='test',
  serialized_pb=_b('\n\ntest.proto\x12\x04test\x1a\x10struct_map.proto\"\x13\n\x03Str\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\t\"\x13\n\x03\x42in\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\"\x13\n\x03Int\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x05\"\x15\n\x05\x46loat\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x01\"\x14\n\x04\x42ool\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x08\"\x15\n\x05\x41rray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\t\"&\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"#\n\x03Map\x12\x1c\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x0e.test.MapEntry\"\xd2\x01\n\x08Struct10\x12\x12\n\nf000000000\x18\x01 \x02(\t\x12\x12\n\nf000000001\x18\x02 \x02(\t\x12\x12\n\nf000000002\x18\x03 \x02(\t\x12\x12\n\nf000000003\x18\x04 \x02(\t\x12\x12\n\nf000000004\x18\x05 \x02(\t\x12\x12\n\nf000000005\x18\x06 \x02(\t\x12\x12\n\nf000000006\x18\x07 \x02(\t\x12\x12\n\nf000000007\x18\x08 \x02(\t\x12\x12\n\nf000000008\x18\t \x02(\t\x12\x12\n\nf000000009\x18\n \x02(\t\"\x1a\n\nSimpleList\x12\x0c\n\x04ints\x18\x01 \x03(\x05\"\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x02(\x05\x12\t\n\x01y\x18\x02 \x02(\x05\")\n\nPointsList\x12\x1b\n\x06points\x18\x01 \x03(\x0b\x32\x0b.test.Point')
  ,
  dependencies=[struct_map_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STR = _descriptor.Descriptor(
  name='Str',
  full_name='test.Str',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.Str.data', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=57,
)


_BIN = _descriptor.Descriptor(
  name='Bin',
  full_name='test.Bin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.Bin.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=78,
)


_INT = _descriptor.Descriptor(
  name='Int',
  full_name='test.Int',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.Int.data', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=99,
)


_FLOAT = _descriptor.Descriptor(
  name='Float',
  full_name='test.Float',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.Float.data', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=122,
)


_BOOL = _descriptor.Descriptor(
  name='Bool',
  full_name='test.Bool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.Bool.data', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=144,
)


_ARRAY = _descriptor.Descriptor(
  name='Array',
  full_name='test.Array',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.Array.data', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=167,
)


_MAPENTRY = _descriptor.Descriptor(
  name='MapEntry',
  full_name='test.MapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test.MapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='test.MapEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=207,
)


_MAP = _descriptor.Descriptor(
  name='Map',
  full_name='test.Map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.Map.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=244,
)


_STRUCT10 = _descriptor.Descriptor(
  name='Struct10',
  full_name='test.Struct10',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='f000000000', full_name='test.Struct10.f000000000', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f000000001', full_name='test.Struct10.f000000001', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f000000002', full_name='test.Struct10.f000000002', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f000000003', full_name='test.Struct10.f000000003', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f000000004', full_name='test.Struct10.f000000004', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f000000005', full_name='test.Struct10.f000000005', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f000000006', full_name='test.Struct10.f000000006', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f000000007', full_name='test.Struct10.f000000007', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f000000008', full_name='test.Struct10.f000000008', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='f000000009', full_name='test.Struct10.f000000009', index=9,
      number=10, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=457,
)


_SIMPLELIST = _descriptor.Descriptor(
  name='SimpleList',
  full_name='test.SimpleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ints', full_name='test.SimpleList.ints', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=459,
  serialized_end=485,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='test.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='test.Point.x', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='test.Point.y', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=487,
  serialized_end=516,
)


_POINTSLIST = _descriptor.Descriptor(
  name='PointsList',
  full_name='test.PointsList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='test.PointsList.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=518,
  serialized_end=559,
)

_MAP.fields_by_name['data'].message_type = _MAPENTRY
_POINTSLIST.fields_by_name['points'].message_type = _POINT
DESCRIPTOR.message_types_by_name['Str'] = _STR
DESCRIPTOR.message_types_by_name['Bin'] = _BIN
DESCRIPTOR.message_types_by_name['Int'] = _INT
DESCRIPTOR.message_types_by_name['Float'] = _FLOAT
DESCRIPTOR.message_types_by_name['Bool'] = _BOOL
DESCRIPTOR.message_types_by_name['Array'] = _ARRAY
DESCRIPTOR.message_types_by_name['MapEntry'] = _MAPENTRY
DESCRIPTOR.message_types_by_name['Map'] = _MAP
DESCRIPTOR.message_types_by_name['Struct10'] = _STRUCT10
DESCRIPTOR.message_types_by_name['SimpleList'] = _SIMPLELIST
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['PointsList'] = _POINTSLIST

Str = _reflection.GeneratedProtocolMessageType('Str', (_message.Message,), dict(
  DESCRIPTOR = _STR,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Str)
  ))
_sym_db.RegisterMessage(Str)

Bin = _reflection.GeneratedProtocolMessageType('Bin', (_message.Message,), dict(
  DESCRIPTOR = _BIN,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Bin)
  ))
_sym_db.RegisterMessage(Bin)

Int = _reflection.GeneratedProtocolMessageType('Int', (_message.Message,), dict(
  DESCRIPTOR = _INT,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Int)
  ))
_sym_db.RegisterMessage(Int)

Float = _reflection.GeneratedProtocolMessageType('Float', (_message.Message,), dict(
  DESCRIPTOR = _FLOAT,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Float)
  ))
_sym_db.RegisterMessage(Float)

Bool = _reflection.GeneratedProtocolMessageType('Bool', (_message.Message,), dict(
  DESCRIPTOR = _BOOL,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Bool)
  ))
_sym_db.RegisterMessage(Bool)

Array = _reflection.GeneratedProtocolMessageType('Array', (_message.Message,), dict(
  DESCRIPTOR = _ARRAY,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Array)
  ))
_sym_db.RegisterMessage(Array)

MapEntry = _reflection.GeneratedProtocolMessageType('MapEntry', (_message.Message,), dict(
  DESCRIPTOR = _MAPENTRY,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.MapEntry)
  ))
_sym_db.RegisterMessage(MapEntry)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), dict(
  DESCRIPTOR = _MAP,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Map)
  ))
_sym_db.RegisterMessage(Map)

Struct10 = _reflection.GeneratedProtocolMessageType('Struct10', (_message.Message,), dict(
  DESCRIPTOR = _STRUCT10,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Struct10)
  ))
_sym_db.RegisterMessage(Struct10)

SimpleList = _reflection.GeneratedProtocolMessageType('SimpleList', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLELIST,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.SimpleList)
  ))
_sym_db.RegisterMessage(SimpleList)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), dict(
  DESCRIPTOR = _POINT,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.Point)
  ))
_sym_db.RegisterMessage(Point)

PointsList = _reflection.GeneratedProtocolMessageType('PointsList', (_message.Message,), dict(
  DESCRIPTOR = _POINTSLIST,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:test.PointsList)
  ))
_sym_db.RegisterMessage(PointsList)


# @@protoc_insertion_point(module_scope)
