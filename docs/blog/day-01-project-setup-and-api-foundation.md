# Day 01 – Project Setup and API Foundation

## Overview

Today's work established the foundational structure and minimal API surface for a production-ready backend service. Rather than jumping into features, we focused on creating a scalable project organization, configuration management, developer tooling, and a single operational endpoint that demonstrates core backend engineering principles. This foundation supports all future development without requiring structural refactoring.

## The Real-World Problem

Production backend systems require structure from day one. Without clear organization, codebases become unmaintainable as they grow. Router-based architecture allows teams to work on different features independently. Health check endpoints are essential for monitoring, load balancers, and deployment pipelines. Configuration management ensures the application adapts to different environments without code changes. API versioning from the start prevents costly refactoring when breaking changes become necessary. Developer tooling reduces cognitive load and ensures consistent workflows across the team.

## What Was Built

- Established project structure with clear separation of concerns (app, tests, docs)
- Created minimal FastAPI application with router-based organization
- Implemented `GET /api/v1/health` endpoint for operational monitoring
- Set up configuration management using `pydantic-settings` with environment variable support
- Added CORS middleware for local frontend development
- Configured lifespan handler for startup and shutdown events (replacing deprecated `on_event`)
- Created `.env.example` template for environment configuration
- Added developer tooling via a Makefile (`run`, `run2`, `kill`, `test`, `fmt`)
- Configured code formatting and linting with ruff
- Added pytest testing infrastructure with a health endpoint test
- Configured API versioning with `/api/v1` prefix
- Verified setup through Swagger UI and curl testing

## Key Backend Concepts

### Router-Based Organization

Even with a single endpoint, organizing routes through FastAPI's `APIRouter` establishes patterns that scale. In production, different teams often own different routers (users, orders, payments), allowing parallel development without merge conflicts. Routers also enable middleware, authentication, and rate limiting to be applied selectively to different API groups. This pattern makes it clear where new endpoints belong and prevents early technical debt.

### Health Check Endpoints

The `/health` endpoint serves multiple critical functions in production systems. Load balancers use it to determine if an instance should receive traffic. Monitoring systems poll it to detect service degradation. Deployment pipelines verify it before marking a deployment successful. Kubernetes uses health checks for liveness and readiness probes. A simple endpoint that returns `{"status": "ok"}` becomes the foundation for operational visibility.

### Configuration Management

Using `pydantic-settings` for configuration ensures type safety and environment-specific behavior. Settings are loaded from environment variables with `.env` file support for local development. This pattern allows the same codebase to run in development, staging, and production with different configurations. Sensitive values are never hardcoded. The `Settings` class centralizes configuration and validates it at startup, preventing runtime configuration errors.

### CORS Middleware

Cross-Origin Resource Sharing (CORS) middleware enables frontend applications running on different ports to communicate with the backend. In development, this allows local frontend servers (Vite, Next.js) to make API calls without browser security errors. In production, allowed origins are restricted to trusted domains. While often handled at the gateway layer, having CORS configured in the application provides flexibility and clarity.

### Lifespan Events

FastAPI’s lifespan handler (implemented with `asynccontextmanager`) replaces the deprecated `on_event` decorator. It provides a clean, explicit way to manage startup and shutdown logic such as logging, database connections, or background services. This pattern is easier to test and becomes essential as more infrastructure is added.

### Developer Tooling

A Makefile provides consistent, documented commands for common tasks: running the server, running tests, formatting code, and managing ports. This reduces cognitive overhead and ensures everyone uses the same workflows. Port helpers (`run`, `run2`, `kill`) make local development smoother when running multiple services.

### Code Quality Tooling

Ruff provides fast linting and formatting with a single tool, configured via `pyproject.toml`. Automated formatting prevents style drift and reduces friction during code review. Running `make fmt` ensures the codebase remains clean and consistent as it grows.

### Testing Infrastructure

Pytest provides the testing framework, with FastAPI’s test client enabling endpoint testing without running a live server. The initial health endpoint test establishes the testing pattern that future endpoints will follow. Testing from day one ensures refactors remain safe and encourages confidence in change.

### API Versioning Strategy

The `/api/v1` prefix establishes versioning from the first endpoint. When breaking changes are needed, new versions can be introduced without disrupting existing clients. Versioning early avoids difficult tradeoffs later and is a standard production practice.

### Project Structure Before Features

Starting with a clear directory structure (`app`, `tests`, `docs`, `core`) prevents decision fatigue and signals maintainability to other engineers and hiring managers. The structure established here will support databases, background jobs, and additional services without reorganization.

## What Tripped Me Up

Day 01 was intentionally minimal. The primary decision was choosing router-based organization over a single-file app. While a single file would have been simpler initially, routers avoid technical debt as the codebase grows.

Additionally, replacing FastAPI’s deprecated `on_event` with lifespan handlers required understanding `asynccontextmanager`, but resulted in a cleaner, more future-proof implementation.

## How This Scales in Real Systems

At scale, the patterns introduced today become critical infrastructure:

- Health checks evolve to include database and dependency status
- Routers map cleanly to service boundaries and team ownership
- Configuration management prevents environment drift
- CORS rules become part of the security perimeter
- Lifespan handlers manage complex startup sequences
- Tooling integrates directly into CI/CD pipelines
- Linting and tests act as automated quality gates
- API versioning enables long-lived client support

The foundation laid on Day 01 mirrors patterns used by large-scale production systems. Starting with structure, clarity, and tooling allows features to grow without chaos.

## What's Next

The next step is introducing user-facing endpoints with validation and request schemas. The foundation established here will remain unchanged, demonstrating how strong infrastructure supports evolving business logic.
