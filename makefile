activate:
	pipenv shell

run:
	docker-compose up -d postgres-dev
	export ENV=development && uvicorn main:app --reload --host 0.0.0.0

clean-dev:
	docker-compose stop postgres-dev
	docker-compose rm -f postgres-dev
	docker volume rm backend_pgdata

generate_requirements_txt:
	pipenv requirements --dev  > requirements.txt

test:
	docker-compose up -d postgres-test
	./wait-for-postgres.sh
	export ENV=testing && pytest tests -s -x -vv
	docker-compose stop postgres-test
	docker-compose rm -f postgres-test

test-coverage:
	docker-compose up -d postgres-test
	./wait-for-postgres.sh
	export ENV=testing && pytest tests -x -vv --cov=. --cov-report=term-missing
	docker-compose stop postgres-test
	docker-compose rm -f postgres-test

install:
	pipenv install --dev

format:
	black . 

lint:
	pylint *.py