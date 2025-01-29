from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)
@app.get("/")
async def root():
    # Get current date and time
    iso_timestamp = datetime.now().isoformat()
    #
    # {
    #   "email": "your-email@example.com",
    #   "current_datetime": "2025-01-30T09:30:00Z",
    #   "github_url": "<https://github.com/yourusername/your-repo>"
    # }
    return {"email": "x10tion007@mail.com",
            "current_datetime": iso_timestamp,
            "github_url": "https://github.com/0x00whitecode/HNG_TASK001_BASIC_INFO"
            }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
