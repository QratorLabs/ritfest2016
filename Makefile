.PHONY: help gendata codegen_google_proto codegen_apache_thrift codegen_fb_thrift codegen pyavroc requirements requirements_fb_thrift

help:
	@echo 'Run `make [gendata|codegen|requirements|requirements_fb_thrift]`'

gendata:
	./gen_data.py

codegen_google_proto:
	$(eval TEMPDIR := $(shell mktemp -d))
	docker run --rm -v "`pwd`":/root/src -v "$(TEMPDIR)":/root/dst python:3.4 /root/src/codegen.sh google_proto
	cp -r "$(TEMPDIR)"/* codegen/

codegen_apache_thrift:
	$(eval TEMPDIR := $(shell mktemp -d))
	docker run --rm -v "`pwd`":/root/src -v "$(TEMPDIR)":/root/dst python:3.4 /root/src/codegen.sh apache_thrift
	cp -r "$(TEMPDIR)"/* codegen/

codegen_fb_thrift:
	$(eval TEMPDIR := $(shell mktemp -d))
	docker run --rm -v "`pwd`":/root/src -v "$(TEMPDIR)":/root/dst python:3.4 /root/src/codegen.sh fb_thrift
	cp -r "$(TEMPDIR)"/* codegen/

codegen: codegen_google_proto codegen_apache_thrift codegen_fb_thrift

pyavroc:
	# Make and copy pyavroc
	$(eval TEMPDIR := $(shell mktemp -d))
	docker run --rm -v "`pwd`":/root/src -v "$(TEMPDIR)":/root/dst python:3.4 /root/src/make_pyavroc.sh
	cp -r "$(TEMPDIR)"/* codegen/

requirements:
	pip2 install --upgrade -r requirements2.txt
	pip3 install --upgrade -r requirements3.txt

	# 2to3 `protobuf` and install it
	$(eval TEMPDIR := $(shell mktemp -d))
	cd "$(TEMPDIR)"; wget "https://pypi.python.org/packages/2c/05/10c2611da9149677abfae24e208761794561e406c37d78c36bd8dda8ea80/protobuf-2.6.1.tar.gz#md5=6bf843912193f70073db7f22e2ea55e2" -O - | tar xvzf -; cd "protobuf-2.6.1"; 2to3 -w .; cat setup.py | grep -v 'setup_requires' > setup.new; mv setup.new setup.py; pip3 install .
	rm -rf "$(TEMPDIR)"

	# Apache avro for python3 not in pypi
	$(eval TEMPDIR := $(shell mktemp -d))
	cd "$(TEMPDIR)"; wget "http://apache.org/dist/avro/avro-1.8.0/py3/avro-python3-1.8.0.tar.gz" -O - | tar xvzf -; cd "avro-python3-1.8.0"; pip3 install .
	rm -rf "$(TEMPDIR)"

requirements_fb_thrift:
	pip2 uninstall -y thrift || true

	$(eval TEMPDIR := $(shell mktemp -d))
	cd "$(TEMPDIR)"; wget "https://github.com/facebook/fbthrift/archive/v0.31.0.tar.gz" -O - | tar xvzf -; cd "fbthrift-0.31.0/thrift/lib/py"; pip2 install .; pip3 install .
	rm -rf "$(TEMPDIR)"
