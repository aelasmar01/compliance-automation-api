# Compliance Automation API

A Python-based backend service that simulates an internal compliance system used to verify if user accounts meet IAM and data-handling policies. Built with **FastAPI**, **SQLAlchemy**, and **Alembic**, this API forms the foundation for later phases like JWT authentication, policy logic, and automated compliance checks.

---

## Phase 1 — Domain & Data Modeling

**Goal:** Design the project’s data layer and ensure migrations work reliably.

### ✅ Deliverables
- Database schema with three core tables:
  - `users` — stores account info and roles  
  - `policies` — defines compliance rules as JSON criteria  
  - `compliance_results` — links users to policy checks with PASS/FAIL status  
- SQLAlchemy ORM models and relationships  
- SQLite database for local development  
- Alembic migrations for schema versioning  
- Basic test insertions to verify ORM functionality  

---

## Tech Stack

| Layer | Tool |
|-------|------|
| API Framework | FastAPI |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Auth (coming in Phase 2) | JWT |
| Secrets | python-dotenv |
| Password Hashing | passlib (PBKDF2) |
| Containerization (later) | Docker |

---

## Project Structure

```
compliance-api/
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── models.py
│   └── main.py
├── alembic/
│   └── versions/
├── alembic.ini
├── .env
├── dev.db
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1 Clone and create virtual environment
```bash
git clone https://github.com/<your-username>/compliance-automation-api.git
cd compliance-automation-api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2 Configure `.env`
```bash
DATABASE_URL=sqlite:///./dev.db
```

### 3 Initialize and migrate database
```bash
alembic upgrade head
```

### 4 Verify ORM works
```bash
python - <<'PY'
from app.db import SessionLocal
from app.models import User, Policy
from passlib.hash import pbkdf2_sha256
db = SessionLocal()
u = User(username="alice", email="alice@example.com", hashed_password=pbkdf2_sha256.hash("ChangeMe123!"))
p = Policy(name="MFA Required", description="User must have MFA enabled", criteria={"require_mfa": True})
db.add_all([u, p]); db.commit()
print("Users:", db.query(User).count(), "Policies:", db.query(Policy).count())
db.close()
PY
```
Expected output:
```
Users: 1 Policies: 1
```

---

## 🦯 Next Phase Preview
**Phase 2: Authentication & Core Endpoints**
- Implement JWT-based authentication  
- Add `/users`, `/policies`, `/compliance-check` routes  
- Enforce role-based access control (admin vs user)  
- Begin unit testing  

---

## 📄 License
MIT License © 2025 Ali El-Asmar

