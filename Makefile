install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

test:
	poetry run pytest

lint:
	poetry run flake8 hexlet_python_package

package-install:
	python3 -m pip install --user dist/*.whl