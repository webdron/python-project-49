brain-games:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install dist/*.whl --break-system-packages
make lint:
	poetry run flake8 brain_games

