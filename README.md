# Velox

An image and video sharing platform. This repo is the backend API, built with Python and FastAPI.

Velox is an early-stage project. I am building it to learn how real APIs are designed, tested and documented.

## Status

In progress. [One line on what works today, e.g. "Image upload and retrieval work. Auth is next."]

## Tech Stack

- Python (version pinned in `.python-version`)
- FastAPI
- uv for dependency management

## Getting Started

1. Clone the repo

```bash
git clone https://github.com/0rukpa/velox.git
cd velox
```

2. Install dependencies

```bash
uv sync
```

3. Run the server

```bash
uv run uvicorn main:app --reload
```

[Check this command matches how you actually start the app. If your FastAPI app lives in `src/app`, adjust the module path.]

4. Open the interactive docs

FastAPI generates docs automatically. Once the server is running, go to:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | What it does |
| ------ | -------- | ------------ |
| [GET] | [/endpoint] | [Short description] |
| [POST] | [/endpoint] | [Short description] |

[Fill in one row per endpoint that works. Delete the brackets. Only list what exists.]

## How I Test It

I test each endpoint by sending real requests and checking the response body and the HTTP status code. For example:

```bash
curl -i http://127.0.0.1:8000/[endpoint]
```

I also use the `/docs` page to try requests in the browser.

## What I Learned

- How to read documentation and use it to build, instead of only following tutorials
- How to design and build REST APIs with FastAPI
- What HTTP status codes actually mean, by sending requests and reading the responses (for example 200, 404 and 422)
- How to structure a Python project and manage it with uv

## Roadmap

- [ ] [Next feature, e.g. user authentication]
- [ ] [Next feature, e.g. image storage]
- [ ] [Next feature, e.g. tests]

## Author

Light Orukpa Diamonds
GitHub: [@0rukpa](https://github.com/0rukpa)