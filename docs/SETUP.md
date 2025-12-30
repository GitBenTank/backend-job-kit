# Setup Commands - Day 1

## Create Python Virtual Environment

```bash
python3 -m venv venv
```

## Activate Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

The `--reload` flag enables auto-reload on code changes (development only).

## Test Health Check Endpoint

Once the server is running, visit:
- **API Endpoint**: http://localhost:8000/api/v1/health
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## Verify It Works

```bash
curl http://localhost:8000/api/v1/health
```

Expected response:
```json
{"status":"healthy","service":"backend-job-kit"}
```

