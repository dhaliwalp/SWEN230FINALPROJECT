# SWEN230FINALPROJECT
Web Scraping Flask Application

docker build -t flask-docker .
docker run -d -p 9090:9090 --name my-flask-app flask-docker

docker logs flask_ex1_con -f

docker:
	docker build -t flask_230 .
	docker run -itd -p 9090:9090 --rm -v ${PWD}/app:/src/app --name flask_230_con flask_230
	docker logs flask_230_con -f


docker:
	docker build -t flask_ex1 .
	docker run -itd -p 9090:9090 --rm -v ${PWD}/app:/src/app --name flask_ex1_con flask_ex1
	docker logs flask_ex1_con -f