# A testing environment

FROM redis:6.0

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -qy python3 python3-pip
RUN python3 -m pip install setuptools

ADD redlog/ /opt/redlog/
ADD *.py README.md /opt/
RUN cd /opt && python3 setup.py install

WORKDIR /opt
ENTRYPOINT redis-server & python3 -m unittest -v test.py && python3 -m redlog
