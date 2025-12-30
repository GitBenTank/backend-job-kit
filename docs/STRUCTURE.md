# FastAPI App Structure - Day 1

## Proposed File Tree

```
backend-job-kit/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app instance + root routes
│   └── routers/
│       ├── __init__.py
│       └── health.py    # Health check endpoint
├── tests/
│   └── __init__.py
├── requirements.txt     # Dependencies
└── README.md
```

## Why This Structure Works for Real Backend Jobs

1. **Router-based organization**: Even with one endpoint, using `routers/` shows you understand FastAPI's APIRouter pattern. This is how production apps scale.

2. **Separation of concerns**: `main.py` handles app setup; `routers/` handles route logic. This pattern is standard in FastAPI codebases.

3. **Test-ready**: The `tests/` directory is already in place. Hiring managers look for developers who think about testing from day one.

4. **Scalable foundation**: Adding new features (users, products, etc.) means adding new router files, not cramming everything into `main.py`.

5. **Industry standard**: This mirrors how FastAPI is used at companies like Netflix, Uber, and Microsoft (FastAPI's sponsors).

## What We're NOT Doing (Yet)

- No `models/` - no database yet
- No `schemas/` - no Pydantic models yet (we'll add when we need validation)
- No `services/` - no business logic layer yet
- No `config.py` - no environment variables yet

We add these as we need them, not preemptively.

