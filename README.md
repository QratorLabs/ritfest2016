# Benchmark tool for serialization libraries for python

http://backendconf.ru/2016/abstracts/2137.html

## Prepare your environment

1. `make gendata` - [re]generates test data.

2. `make codegen` - runs compile & code gen in one-time docker container.

3. `make pyavroc` - compile `pyavroc` library in one-time docker container.

4. `make requirements` - Install required python libraries via pip2 and pip3. Prepare your `virtualenv` before executing this.

5. `make codegen_fb_thrift` - Replace `apache thrift` with `facebook thrift`.

## Run tests

`./measure_size.py` — outputs CSV with sizes of data types.

`./measure.py` — outputs CSV with serialization timings. Use `--no-cython` option to disable `Cython` in `Thriftpy`.
