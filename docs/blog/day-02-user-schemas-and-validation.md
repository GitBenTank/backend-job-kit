# Day 02 – User Schemas, Validation, and API Contracts

## Overview

Today's work focused on designing stable API contracts and enforcing validation at the application boundary before introducing persistence. This approach mirrors how production systems are often built: define the interface first, then implement persistence.

## The Real-World Problem

In production systems, API contracts are the contract between services and clients. Once published, changing them breaks consumers. Validation at the API boundary prevents invalid data from entering the system, reducing downstream errors and improving debugging. Separating input and output schemas prevents clients from controlling server-managed fields (like IDs or timestamps) and allows the API to evolve independently of internal data structures.

## What Was Built

- Defined `UserCreate` and `UserRead` Pydantic models with explicit separation of input vs output schemas
- Introduced `POST /api/v1/users` endpoint with email validation and duplicate detection
- Added `GET /api/v1/users/{user_id}` endpoint with proper 404 handling
- Used in-memory dictionary storage to focus on API design without persistence complexity
- Registered endpoints under `/api/v1` prefix for versioning
- Verified behavior through Swagger UI and curl testing

## Key Backend Concepts

### Input/Output Schema Separation

Separating `UserCreate` (input) from `UserRead` (output) is a common pattern in production APIs. Clients can only provide fields they control (email, name), while the server manages fields like `id` and `is_active`. This prevents clients from setting internal state and allows the API to add fields to responses without breaking clients. In microservices, this separation also enables different services to have different views of the same entity.

### Validation at the Boundary

Pydantic validates incoming requests before they reach business logic. Using `EmailStr` ensures email format validation happens at the API layer, not in application code. This "fail fast" approach means invalid requests are rejected immediately with clear error messages, rather than causing subtle bugs downstream. In production, this validation layer often includes rate limiting, authentication checks, and request sanitization.

### API Versioning

The `/api/v1` prefix allows the API to evolve without breaking existing clients. When breaking changes are needed, a new version (`/api/v2`) can be introduced while maintaining backward compatibility. This is critical in production systems where multiple clients depend on the API.

## What Tripped Me Up

### Missing email-validator Dependency

After implementing `EmailStr` in the Pydantic model, the FastAPI server crashed during startup with an import error. The traceback clearly indicated that `email-validator` was missing, even though `EmailStr` is part of Pydantic's API.

**What happened:** `EmailStr` requires the optional `email-validator` package, which isn't installed by default with Pydantic. The server failed during schema generation, before any requests could be handled.

**Why it happened:** Pydantic keeps email validation as an optional dependency to keep the core package lightweight. This is common in Python ecosystems where packages have "extras" for optional features.

**How it was fixed:** Installed `email-validator` via pip and updated `requirements.txt` using `pip freeze`. This dependency management issue is typical in backend work—the code was correct, but the environment was incomplete.

**Takeaway:** Reading tracebacks carefully and understanding optional dependencies are essential backend skills. This debugging process demonstrated the same problem-solving approach needed in production environments. This reinforced that production-ready validation often depends on optional dependencies that must be explicitly managed.

## How This Scales in Real Systems

At scale, API validation becomes a critical performance and security concern. Production systems often use:

- **Schema validation libraries** (like Pydantic) that are fast enough to handle thousands of requests per second
- **API gateways** that perform validation before requests reach application servers
- **Schema registries** that ensure consistency across multiple services
- **Contract testing** to verify API schemas match between services

The in-memory storage used today would be replaced with a database, but the API contract remains unchanged. This separation allows the persistence layer to evolve (e.g., migrating from SQL to NoSQL) without breaking API consumers.

Versioning becomes more complex at scale: multiple API versions may run simultaneously, requiring careful routing and deprecation strategies. The `/api/v1` prefix established today sets the foundation for this evolution.

## What's Next

Tomorrow we'll add PostgreSQL and SQLAlchemy to replace the in-memory storage. The API contracts defined today will remain unchanged—demonstrating how proper schema separation allows the persistence layer to evolve independently. We'll also explore database migrations and connection pooling, which are essential for production database operations.

