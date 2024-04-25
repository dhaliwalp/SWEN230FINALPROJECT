build:
	docker build -t flask-app . 

run:
	docker run -p 9090:9090 flask-app

clean:
	docker rm -f $$(docker ps -aq)

.PHONY: build run clean