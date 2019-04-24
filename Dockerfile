FROM ubuntu:16.04

# docker build -t vanessa/banner-maker .

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

RUN mkdir -p /code
WORKDIR /code
ADD . /code

RUN pip install flask

ENTRYPOINT ["python"]
CMD ["/code/index.py"]
