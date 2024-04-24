build:
	docker build -t flask-docker .

run:
	docker run -p 9090:9090 -v $(PWD):/app flask-docker

clean:
	docker rmi -f flask-docker