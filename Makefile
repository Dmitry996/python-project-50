install:
	poetry install

publish:
	poetry publish --dry-run

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall dist/*.whl

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build