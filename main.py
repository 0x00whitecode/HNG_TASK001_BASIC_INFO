from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from datetime import datetime, timezone

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/", status_code=200)
async def root():
    # Get current date and time in ISO 8601 format
    iso_timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    data = {
        "email": "x10tion007@mail.com",
        "current_datetime": iso_timestamp,
        "github_url": "https://github.com/0x00whitecode/HNG_TASK001_BASIC_INFO"
    }

    return JSONResponse(content=data)
