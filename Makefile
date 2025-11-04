install:
	pip install -r requirements.txt

test:
	pytest

format:
	black src tests

lint:
	flake8 src tests

run:
	python -m src --simulate
