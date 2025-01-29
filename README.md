# FastAPI Basic Info API

This is a simple FastAPI application that provides basic information, including the current date and time, and a greeting endpoint. The application is designed to be accessible from any origin using CORS middleware.

## Features
- Serves basic API endpoints with FastAPI.
- Supports CORS for cross-origin requests.
- Provides the current date and time in ISO format.
- Returns a personalized greeting message.

## Technologies Used
- Python 3.x
- FastAPI
- Uvicorn (for running the server)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/0x00whitecode/HNG_TASK001_BASIC_INFO.git
   cd HNG_TASK001_BASIC_INFO
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install fastapi uvicorn
   ```

## Running the Application

Start the FastAPI server using Uvicorn:
```sh
uvicorn main:app --reload
```

The application will be available at:
- **Swagger UI (API Documentation):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc UI:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### Root Endpoint
- **URL:** `/`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "email": "x10tion007@mail.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/0x00whitecode/HNG_TASK001_BASIC_INFO"
  }
  ```


## CORS Configuration
The application allows cross-origin requests from any domain using the `CORSMiddleware` configuration:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

For more information about hiring Python developers, visit [HNG Python Developer Hiring](https://hng.tech/hire/python-developers).

### Additional Links:
- [Hire C# Developers](https://hng.tech/hire/csharp-developers)
- [Hire Golang Developers](https://hng.tech/hire/golang-developers)
- [Hire PHP Developers](https://hng.tech/hire/php-developers)
- [Hire Java Developers](https://hng.tech/hire/java-developers)
- [Hire Node.js Developers](https://hng.tech/hire/nodejs-developers)

## License
This project is open-source and available under the [MIT License](LICENSE).

## Author
- **Email:** x10tion007@mail.com
- **GitHub:** [0x00whitecode](https://github.com/0x00whitecode/)
