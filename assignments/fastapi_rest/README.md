# 🚀 Building REST APIs with FastAPI

## 🎯 Objective

Create a small REST API using the FastAPI framework to practice defining endpoints, request/response models, and input validation.

## 📝 Tasks

### 🛠️ Implement core API endpoints

#### Description
Create endpoints to manage a simple `Item` resource: list items, retrieve a single item by id, create a new item, and delete an item.

#### Requirements
Completed project should:

- Define a Pydantic model for `Item` with `id: int`, `name: str`, and optional `description: str`.
- Implement endpoints:
  - `GET /items` — return list of items
  - `GET /items/{id}` — return a single item or 404
  - `POST /items` — accept an `Item` (without `id`) and return created item with assigned `id`
  - `DELETE /items/{id}` — remove an item and return a success response
- Validate request data using Pydantic models and return appropriate HTTP status codes.
- Ensure responses are JSON serializable and include correct status codes.

### 🛠️ Run and document the API

#### Description
Run the app locally with Uvicorn and verify the interactive API docs are available.

#### Requirements

- Provide instructions to run the server (e.g., `uvicorn assignments.fastapi_rest.starter_code:app --reload`).
- Confirm the automatic OpenAPI docs are reachable at `/docs`.

---

If you provide starter code, register it using the repository helper scripts and include an attachment named `Starter Code`.
