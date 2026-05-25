# 🚀 FastAPI Production-Level Boilerplate

A scalable and production-ready backend API built using FastAPI, PostgreSQL, Async SQLAlchemy, JWT Authentication, RBAC (Role-Based Access Control), Redis Cache, Docker, and Clean Architecture.

---

# 📌 Features

## ✅ Authentication & Authorization
- JWT Access Token
- Refresh Token System
- User Login/Register
- Password Hashing
- Role-Based Access Control (RBAC)
- Permission-Based APIs

---

## ✅ Database Features
- PostgreSQL
- Async SQLAlchemy
- Alembic Migrations
- UUID Primary Keys
- Soft Delete
- Relationships & Foreign Keys

---

## ✅ API Features
- CRUD APIs
- Pagination
- Search
- Sorting
- Filtering
- API Versioning

---

## ✅ Security
- JWT Authentication
- Password Encryption
- CORS Middleware
- Request Validation
- Rate Limiting

---

## ✅ Performance
- Redis Cache
- Background Tasks
- Async APIs
- Connection Pooling

---

## ✅ DevOps
- Docker Support
- Docker Compose
- Environment Variables
- Production Ready Structure

---

## ✅ Testing
- Pytest
- API Testing
- Authentication Testing

---

# 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| FastAPI | Backend Framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Alembic | Database Migration |
| Redis | Caching |
| Docker | Containerization |
| JWT | Authentication |
| Pytest | Testing |

---

# 📁 Project Structure

```bash
app/
├── api/
│   ├── v1/
│   ├── deps/
│   └── routes/
│
├── core/
│   ├── config.py
│   ├── security.py
│   └── database.py
│
├── models/
├── schemas/
├── repositories/
├── services/
├── middleware/
├── utils/
├── auth/
├── tests/
├── migrations/
├── logs/
└── main.py
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/fastapi-rbac-boilerplate.git

cd fastapi-rbac-boilerplate
```

---

## 2️⃣ Create Virtual Environment

### Using UV

```bash
uv venv
```

Activate Environment

### Linux / Mac

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

# 🐳 Docker Setup

## Run Docker Containers

```bash
docker-compose up --build
```

---

# 🗄️ Database Migration

## Create Migration

```bash
alembic revision --autogenerate -m "Initial migration"
```

## Run Migration

```bash
alembic upgrade head
```

---

# ▶️ Run Application

```bash
uvicorn app.main:app --reload
```

---

# 📚 API Documentation

| Documentation | URL |
|---|---|
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

---

# 🔐 Authentication APIs

| Method | Endpoint | Description |
|---|---|---|
| POST | /api/v1/auth/register | Register User |
| POST | /api/v1/auth/login | Login User |
| POST | /api/v1/auth/refresh | Refresh Token |
| POST | /api/v1/auth/logout | Logout User |

---

# 👮 RBAC APIs

## Roles
- Super Admin
- Admin
- Manager
- Employee
- Customer

---

## Permission Examples

```json
{
  "name": "create_user"
}
```

---

# 📦 CRUD Modules

## Included Modules
- Users
- Roles
- Permissions
- Products
- Categories
- Orders

---

# 📄 Example API Response

```json
{
  "success": true,
  "message": "User created successfully",
  "data": {
    "id": "uuid"
  }
}
```

---

# 🔍 Query Features

## Pagination

```bash
GET /users?page=1&limit=10
```

## Search

```bash
GET /users?search=john
```

## Sorting

```bash
GET /users?sort_by=created_at&order=desc
```

---

# ⚡ Redis Cache

Used For:
- User Sessions
- API Cache
- Permission Cache

---

# 🧪 Run Tests

```bash
pytest
```

---

# 🌍 Environment Variables

Create `.env` file:

```env
APP_NAME=FastAPI RBAC
DEBUG=True

DATABASE_URL=postgresql+asyncpg://postgres:password@localhost/db_name

SECRET_KEY=your_secret_key

REDIS_URL=redis://localhost:6379
```

---

# 📌 Health Check API

```bash
GET /health
```

---

# 🔥 Production Features

- Clean Architecture
- Async Database
- Dockerized
- Scalable Structure
- Enterprise Security
- API Versioning
- Structured Logging
- Rate Limiting
- Background Jobs

---

# 📈 Future Improvements

- Multi-Tenant Support
- WebSocket Notifications
- Celery Queue
- Kubernetes Deployment
- CI/CD Pipeline

---

# 👨‍💻 Author

Developed using FastAPI ❤️

---

# 📜 License

MIT License