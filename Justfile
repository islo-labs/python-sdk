# Install dev dependencies
install:
    uv sync --dev

# Run tests
test:
    uv run pytest tests/ -v

# Format
fmt:
    uv run ruff format .

# Lint
lint:
    uv run ruff check .

# Build distributions
build:
    uv build --no-sources

# Verify the SDK imports correctly
verify:
    uv run python -c "from islo import Islo; print('OK')"
