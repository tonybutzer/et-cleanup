#! /bin/bash
for yr in `seq 1950 3 1962`; do  {
	docker run -it tbutzer/drbzip_docker_image python3 tarzip_drb.py $yr &
	docker run -it tbutzer/drbzip_docker_image python3 tarzip_drb.py "$(($yr + 1))" &
	docker run -it tbutzer/drbzip_docker_image python3 tarzip_drb.py "$(($yr + 2))" &
	sleep 7200  # 2hour nap
}; done

