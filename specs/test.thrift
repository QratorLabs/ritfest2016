include "./struct_map.thrift"


struct Str {
    1: required string data,
}

struct Bin {
    1: required binary data,
}

struct Int {
    1: required i32 data,
}

struct Float {
    1: required double data,
}

struct Bool {
    1: required bool data,
}

struct Array {
    1: required list <string> data,
}

struct Map {
    1: required map <string, string> data,
}

struct Struct10 {
    1: required string f000000000,
    2: required string f000000001,
    3: required string f000000002,
    4: required string f000000003,
    5: required string f000000004,
    6: required string f000000005,
    7: required string f000000006,
    8: required string f000000007,
    9: required string f000000008,
    10: required string f000000009,
}

struct SimpleList {
    1: required list<i32> ints,
}

struct PointsList {
    1: required list< list<i32> > points,
}
