#!/bin/bash

set -e

if [ "$1" = "google_proto" ]
then
    build() {
        cd ~
        pip3 install cython cprotobuf protobuf3
        wget "https://github.com/google/protobuf/releases/download/v2.6.1/protobuf-2.6.1.tar.gz" -O - | tar xvzf -
        cd "protobuf-2.6.1"
        ./configure
        make
    }
    gen() {
        cd /root/src/specs/
        mkdir -p /root/dst/google_proto
        /root/protobuf-2.6.1/src/protoc --python_out=/root/dst/google_proto struct_map.proto test.proto
        mkdir -p /root/dst/cprotobuf
        /root/protobuf-2.6.1/src/protoc --cprotobuf_out=/root/dst/cprotobuf struct_map.proto test.proto
        mkdir -p /root/dst/protobuf3_gen
        /root/protobuf-2.6.1/src/protoc --python3_out=/root/dst/protobuf3_gen struct_map.proto test.proto
    }

elif [ "$1" = "apache_thrift" ]
then
    build() {
        cd ~
        wget "http://apache.org/dist/thrift/0.9.3/thrift-0.9.3.tar.gz" -O - | tar xvzf -
        cd "thrift-0.9.3"
        ./configure
        make
    }
    gen() {
        cd /root/src/specs/
        mkdir -p /root/dst/apache_thrift
        /root/thrift-0.9.3/compiler/cpp/thrift --gen py -out /root/dst/apache_thrift test.thrift
        /root/thrift-0.9.3/compiler/cpp/thrift --gen py -out /root/dst/apache_thrift struct_map.thrift
    }

elif [ "$1" = "fb_thrift" ]
then
    build() {
        cd ~
        apt-get update
        apt-get install -y zip cmake libgoogle-glog-dev libdouble-conversion-dev libsnappy-dev flex bison libkrb5-dev libsasl2-dev libnuma-dev libboost-all-dev

        wget "https://github.com/facebook/folly/archive/v0.57.0.zip" -O "v0.57.0.zip"
        unzip "v0.57.0.zip" && rm "v0.57.0.zip"
        (
            cd "folly-0.57.0/folly"
            autoreconf -ivf
            LIBS="-lpthread" ./configure --prefix=/usr
            make
            make install
        )

        wget "https://github.com/facebook/wangle/archive/v0.13.0.zip" -O "v0.13.0.zip"
        unzip "v0.13.0.zip" && rm "v0.13.0.zip"
        (
            cd "wangle-0.13.0/wangle"
            cmake -D CMAKE_INSTALL_PREFIX=/usr .
            make
            make install
        )

        wget "https://github.com/facebook/fbthrift/archive/v0.31.0.zip" -O "v0.31.0.zip"
        unzip "v0.31.0.zip" && rm "v0.31.0.zip"
        (
            cd "fbthrift-0.31.0/thrift"
            autoreconf -ivf
            PYTHON_VERSION=2.7 ./configure
            make
        )
    }
    gen() {
        cd /root/src/specs/
        mkdir -p /root/dst/fb_thrift
        /root/fbthrift-0.31.0/thrift/compiler/thrift1 --gen py -out /root/dst/fb_thrift test.thrift
        /root/fbthrift-0.31.0/thrift/compiler/thrift1 --gen py -out /root/dst/fb_thrift struct_map.thrift
    }

else
    exit 1
fi

build
gen
