install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=term --cov-report=xml

clear-cache:
	find . -type d \( -name '__pycache__' -o -name '.pytest_cache' -o -name '.ruff_cache' \) -exec rm -r {} +
