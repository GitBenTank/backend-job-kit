# Backend Job Kit

A portfolio-grade FastAPI backend project demonstrating real-world backend engineering skills through incremental, production-focused development. Each day builds on the previous work, introducing new concepts while maintaining clean architecture and professional documentation.

## What This Demonstrates

This project showcases backend engineering fundamentals through practical implementation:

- **API Design**: RESTful endpoints with versioning, proper HTTP status codes, and clear request/response contracts
- **Request Validation**: Pydantic models for input validation and schema separation (input vs output models)
- **Error Handling**: Appropriate HTTP status codes and clear error messages
- **Debugging**: Real problem-solving experience with dependency management and runtime errors
- **Documentation**: Technical blog entries explaining design decisions, tradeoffs, and production considerations
- **Code Organization**: Router-based structure that scales to production systems

## Daily Build Log

This project is built incrementally, with each day documented in detail:

- [Day 01: Project Setup and API Foundation](docs/blog/day-01-project-setup-and-api-foundation.md)
- [Day 02: User Schemas, Validation, and API Contracts](docs/blog/day-02-user-schemas-and-validation.md)

Future days will cover database integration (PostgreSQL + SQLAlchemy), migrations, connection pooling, testing strategies, and deployment patterns.

## Project Structure

```
backend-job-kit/
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── models/          # Pydantic models for validation
│   └── routers/         # API route handlers
├── docs/
│   ├── blog/            # Daily technical blog entries
│   ├── daily/           # Quick daily logs
│   ├── skills/          # Skill documentation
│   └── interview/       # Interview preparation notes
└── tests/               # Test suite (coming soon)
```

## Getting Started

See [docs/SETUP.md](docs/SETUP.md) for installation and setup instructions.

## Tech Stack

- **FastAPI**: Modern Python web framework
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server

Future additions: PostgreSQL, SQLAlchemy, Alembic, pytest
