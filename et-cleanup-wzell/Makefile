Image=tbutzer/bzipper_docker_image

cat:
	cat Makefile


build:
	docker build -t ${Image} .


Base=tbutzer/base-miniconda-pangeo

build-base:
	docker build -f Dockerfile.base -t ${Base} .
