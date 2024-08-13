brain-games:
	poetry run brain-games
brain-calc:
	poetry run brain-calc
brain-even:
	poetry run brain-even
brain-gcd:
	poetry run brain-gcd
brain-prime:
	poetry run brain-prime
brain-progression:
	poetry run brain-progression
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --force-reinstall dist/*.whl --break-system-packages
make lint:
	poetry run flake8 brain_games
