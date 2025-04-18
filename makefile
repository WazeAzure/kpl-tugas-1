network:
	docker network create linkinpurry-network

db:
	docker compose up --build linkinpurry-db

web-dev:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build

web-prod:
	docker compose -f docker-compose.yml -f docker-compose.prod.yml up --build

stop:
	docker compose down

reset:
	docker compose down
	docker volume rm linkinpurry-db-data
	docker volume rm linkinpurry-upload-data

