PROJECT_NAME=openai

.PHONY: up
up:
	docker ps -a | awk '/$(PROJECT_NAME)/ { print $$1 }' | xargs docker stop
	docker build --tag openai .
	docker run --env-file .env -d -p 5000:5000 openai

	@echo "Running at http://127.0.0.1:5000/"

.PHONY: down
down: 
	docker ps -a | awk '/$(PROJECT_NAME)/ { print $$1 }' | xargs docker stop
	docker ps -a | awk '/$(PROJECT_NAME)/ { print $$1 }' | xargs docker rm -f
	docker images -a | awk '/$(PROJECT_NAME)/ { print $$3 }' | xargs docker rmi -f

.PHONY: prune
prune:
	docker container prune -f