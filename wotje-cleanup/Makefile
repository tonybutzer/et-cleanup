Image=tbutzer/tarzip_docker_image

cat:
	cat Makefile


run:
	docker run -it ${Image} bash

build:
	docker build -t ${Image} .


Base=tbutzer/base-miniconda-pangeo

build-base:
	docker build -f Dockerfile.base -t ${Base} .
