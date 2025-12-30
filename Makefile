.PHONY: run run2 kill test fmt

PORT ?= 8000

run:
	uvicorn app.main:app --reload --port $(PORT)

run2:
	uvicorn app.main:app --reload --port 8001

kill:
	@lsof -ti:$(PORT) | xargs kill -9 2>/dev/null || echo "No process found on port $(PORT)"

test:
	pytest

fmt:
	ruff format .
	ruff check --fix .

