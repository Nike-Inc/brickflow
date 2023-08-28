black-check:
	@poetry run black --check .

fmt:
	@poetry run black .

check: black-check mypy
	@poetry run prospector --profile prospector.yaml

mypy:
	@poetry run mypy

cov: check
	@poetry ru`n coverage run --source=brickflow --omit "brickflow/sample_dags/*,sample_workflows/*,brickflow/tf/*" -m pytest && \

	poetry run coverage report -m && \
	poetry run coverage xml

gen-bundle-sdk:
	@./tools/gen-bundle.sh
#
#gen-bundle-sdk-v2:
#	@datamodel-codegen  --input brickflow/bundle/output_schema.json --use-title-as-name --input-file-type jsonschema --output brickflow/bundle/model_v2.py

dev:
	@poetry install --all-extras --with dev
	@poetry run pre-commit install
	@poetry run pre-commit install --hook-type pre-push

deploy_env_setup:
	@poetry install --all-extras --with dev

test:
	@poetry run coverage run --source=brickflow --omit "brickflow/bundles/*,brickflow/sample_dags/*,sample_workflows/*,brickflow/tf/*" -m pytest && \
	poetry run coverage report -m && \
	poetry run coverage html

clean:
	@rm -rf dist

build: clean
	@poetry build

poetry:
	@poetry install --all-extras --with dev

coverage: check test

docs:
	@poetry run mike deploy -u dev latest
	@poetry run mike set-default latest
	@poetry run mike serve

deploy-docs:
	@poetry run mike deploy --push --update-aliases $(version) latest

docker-local:
	docker build -t brickflow:latest --build-arg CACHEBUST="$(shell date +%s)" .

poetry-install:
	@pip install --upgrade setuptools && pip install poetry && poetry self add "poetry-dynamic-versioning[plugin]"

get-version:
	@poetry version

requirements:
	@poetry export -f requirements.txt --output requirements.txt --with dev --without-hashes

docker-build:
	@docker build -t brickflow-local .

docker: docker-build
	@docker run -it -v "$(shell pwd)":/brickflow brickflow-local /bin/bash

.PHONY: docs