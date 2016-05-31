from protobuf3.message import Message
from protobuf3.fields import Int32Field, StringField, BoolField, DoubleField, BytesField, MessageField


class Str(Message):
    pass


class Bin(Message):
    pass


class Int(Message):
    pass


class Float(Message):
    pass


class Bool(Message):
    pass


class Array(Message):
    pass


class MapEntry(Message):
    pass


class Map(Message):
    pass


class Struct10(Message):
    pass


class SimpleList(Message):
    pass


class Point(Message):
    pass


class PointsList(Message):
    pass

Str.add_field('data', StringField(field_number=1, required=True))
Bin.add_field('data', BytesField(field_number=1, required=True))
Int.add_field('data', Int32Field(field_number=1, required=True))
Float.add_field('data', DoubleField(field_number=1, required=True))
Bool.add_field('data', BoolField(field_number=1, required=True))
Array.add_field('data', StringField(field_number=1, repeated=True))
MapEntry.add_field('key', StringField(field_number=1, required=True))
MapEntry.add_field('value', StringField(field_number=2, required=True))
Map.add_field('data', MessageField(field_number=1, repeated=True, message_cls=MapEntry))
Struct10.add_field('f000000000', StringField(field_number=1, required=True))
Struct10.add_field('f000000001', StringField(field_number=2, required=True))
Struct10.add_field('f000000002', StringField(field_number=3, required=True))
Struct10.add_field('f000000003', StringField(field_number=4, required=True))
Struct10.add_field('f000000004', StringField(field_number=5, required=True))
Struct10.add_field('f000000005', StringField(field_number=6, required=True))
Struct10.add_field('f000000006', StringField(field_number=7, required=True))
Struct10.add_field('f000000007', StringField(field_number=8, required=True))
Struct10.add_field('f000000008', StringField(field_number=9, required=True))
Struct10.add_field('f000000009', StringField(field_number=10, required=True))
SimpleList.add_field('ints', Int32Field(field_number=1, repeated=True))
Point.add_field('x', Int32Field(field_number=1, required=True))
Point.add_field('y', Int32Field(field_number=2, required=True))
PointsList.add_field('points', MessageField(field_number=1, repeated=True, message_cls=Point))
