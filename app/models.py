from datetime import datetime
from enum import Enum as PyEnum
import os
from sqlalchemy import (
    Column, Integer, String, DateTime, Enum, ForeignKey, Text
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.sqlite import JSON as SQLITE_JSON
from sqlalchemy.dialects.postgresql import JSONB
from app.db import Base

# Choose JSON type based on backend (SQLite in dev, Postgres later)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")
USING_SQLITE = DATABASE_URL.startswith("sqlite")
JSONType = SQLITE_JSON if USING_SQLITE else JSONB

class UserRole(PyEnum):
    user = "user"
    admin = "admin"

class ComplianceStatus(PyEnum):
    PASS_ = "PASS"
    FAIL_ = "FAIL"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(150), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.user)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    results = relationship("ComplianceResult", back_populates="user", cascade="all, delete-orphan")

class Policy(Base):
    __tablename__ = "policies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=True)
    criteria = Column(JSONType, nullable=False, default=dict)
    results = relationship("ComplianceResult", back_populates="policy", cascade="all, delete-orphan")

class ComplianceResult(Base):
    __tablename__ = "compliance_results"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    policy_id = Column(Integer, ForeignKey("policies.id", ondelete="CASCADE"), nullable=False, index=True)
    status = Column(Enum(ComplianceStatus), nullable=False)
    details = Column(JSONType, nullable=True)
    checked_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    user = relationship("User", back_populates="results")
    policy = relationship("Policy", back_populates="results")
