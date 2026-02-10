.PHONY: install test lint clean run-notebook

install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v

lint:
	ruff check src/ tests/
	ruff format src/ tests/ --check

format:
	ruff format src/ tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .ruff_cache

run-notebook:
	jupyter notebook notebooks/
