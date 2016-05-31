#!/bin/bash

set -e

cd ~
apt-get update
apt-get install -y cmake python python-dev python-setuptools

wget "https://github.com/Byhiras/pyavroc/archive/0.7.2.tar.gz" -O - | tar xvzf -
cd pyavroc-0.7.2

mkdir /root/dst/pyavroc

PYTHON=python2 ./clone_avro_and_build.sh --static || true
cp build/lib.linux-x86_64-2.7/pyavroc/_pyavroc.so /root/dst/pyavroc

PYTHON=python3 ./clone_avro_and_build.sh --static || true
cp build/lib.linux-x86_64-3.4/pyavroc/_pyavroc.cpython-34m.so /root/dst/pyavroc
