## 📌 Overview

GitHub Repo Tracker is a backend REST API built using FastAPI and PostgreSQL.  
The service allows users to store and manage GitHub repository information by integrating with the GitHub Public API.

This project demonstrates:
- REST API design
- Database interaction
- External API integration
- Validation and error handling
- Automated testing

---

## 🧠 Problem Understanding & Use Case

### Problem

Build a backend service that:
- Exposes exactly four REST endpoints (POST, GET, PUT, DELETE)
- Stores data in a PostgreSQL database
- Integrates with an external API
- Uses strict request and response validation
- Includes automated tests and documentation

### Chosen Use Case

**GitHub Repository Tracker**

The API fetches repository details from GitHub and stores them locally so they can be retrieved, updated, or deleted later.

---

## ✅ Assumptions

- GitHub public repositories are accessible without authentication
- GitHub API is generally reliable, but may return 404 for invalid repos
- No user authentication is required
- Repository data is identified internally using a numeric ID
- Rate limiting and caching are out of scope for this assignment

---

## 🏗 Design Decisions

### Tech Stack

- **Language:** Python 3.10+
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Testing:** Pytest + FastAPI TestClient

---

### Database Schema

Single table: **repositories**

| Column | Type | Description |
|------|------|------------|
| id | Integer | Primary key |
| name | String | Repository name |
| owner | String | GitHub owner |
| stars | Integer | Star count |
| url | String | GitHub URL |

Indexes are applied to the primary key for fast lookups.

---

### Project Structure

This follows a simple layered architecture:
- API layer (FastAPI routes)
- Business logic (CRUD)
- External service layer (GitHub client)
- Persistence layer (database)

---

## 🔄 API Flow (How the system works)

### POST `/repos`
- User provides GitHub owner and repository name
- API calls GitHub Public API
- Repository details are fetched
- Data is saved to PostgreSQL
- Stored data is returned to the client

### GET `/repos/{repo_id}`
- Fetches repository details from the database

### PUT `/repos/{repo_id}`
- Updates repository name in the database

### DELETE `/repos/{repo_id}`
- Deletes the repository record

---

## ❗ Error Handling Strategy

### 404 Not Found
- Repository not found in database
- Repository not found on GitHub

### 422 Unprocessable Entity
- Invalid request payload

- Database connection issues raise server errors
- External API failures are handled gracefully by returning appropriate responses

---

### 🧪 Testing Strategy
**Integration Tests:** Validate the full request lifecycle (`Request` → `DB` → `Response`).
**Mocking:** External GitHub API calls are **mocked** during testing to ensure reliability and avoid network dependency.

### Tools Used
- Pytest
- FastAPI TestClient

All endpoints are covered with tests to ensure correctness and reliability.
---

## 📌 Example API Calls

### Swagger UI
After running the application, all APIs can be tested using Swagger UI:
http://127.0.0.1:8000/docs

### Create Repository (POST /repos)
curl -X POST http://127.0.0.1:8000/repos \
-H "Content-Type: application/json" \
-d '{
  "owner": "fastapi",
  "repo_name": "fastapi"
}'  

### Get Repository (GET /repos/{id})
curl http://127.0.0.1:8000/repos/1

### Update Repository (PUT /repos/{id})
curl -X PUT http://127.0.0.1:8000/repos/1 \
-H "Content-Type: application/json" \
-d '{
  "name": "fastapi-updated"
}'

### Delete Repository (DELETE /repos/{id})
curl -X DELETE http://127.0.0.1:8000/repos/1


---

## ▶️ How to Run the Project

### 1️⃣ Setup Virtual Environment
bash
python -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create .env file:

DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/githubdb

4️⃣ Run the Server
uvicorn app.main:app --reload

5️⃣ Open API Docs
http://127.0.0.1:8000/docs

## Run Tests
pytest

## Expected result:
4 passed

## Conclusion

1) This project demonstrates a clean backend service with:

2) Proper API design

3) External API integration

4) Database persistence

5) Validation

6) Testing



