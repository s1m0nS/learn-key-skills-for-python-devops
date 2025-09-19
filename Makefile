install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=mylib test_*.py
	
format:
	black *.py mylib/*.py

lint:
	pylint --disable=R,C, --ignore-patterns=test_.*?py *.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refractor: format lint

deploy:
# echo "deploy not yet implemented"

all: install lint test format deploy
