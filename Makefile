install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

clear-cache:
	find ~/python_projects/python-project-50/ -type d -name "__pycache__" -exec rm -r {} +
