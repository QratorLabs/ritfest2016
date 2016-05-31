# coding: utf-8
from cprotobuf import ProtoEntity, Field
# file: test.proto
class Float(ProtoEntity):
    data            = Field('double',	1)

class Bin(ProtoEntity):
    data            = Field('bytes',	1)

class MapEntry(ProtoEntity):
    key             = Field('string',	1)
    value           = Field('string',	2)

class Int(ProtoEntity):
    data            = Field('int32',	1)

class Point(ProtoEntity):
    x               = Field('int32',	1)
    y               = Field('int32',	2)

class SimpleList(ProtoEntity):
    ints            = Field('int32',	1, repeated=True)

class Bool(ProtoEntity):
    data            = Field('bool',	1)

class Struct10(ProtoEntity):
    f000000000      = Field('string',	1)
    f000000001      = Field('string',	2)
    f000000002      = Field('string',	3)
    f000000003      = Field('string',	4)
    f000000004      = Field('string',	5)
    f000000005      = Field('string',	6)
    f000000006      = Field('string',	7)
    f000000007      = Field('string',	8)
    f000000008      = Field('string',	9)
    f000000009      = Field('string',	10)

class Array(ProtoEntity):
    data            = Field('string',	1, repeated=True)

class Str(ProtoEntity):
    data            = Field('string',	1)

class Map(ProtoEntity):
    data            = Field(MapEntry,	1, repeated=True)

class PointsList(ProtoEntity):
    points          = Field(Point,	1, repeated=True)

