install:
	uv sync

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl
