from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # JWT
    JWT_SECRET: str = Field(..., description="32+ char secret for signing JWTs")
    JWT_ALG: str = Field("HS256", description="JWT signing algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(60, ge=1, le=24 * 60)

    # Database
    DATABASE_URL: str = Field("sqlite:///./dev.db")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # ignore stray env vars
    )

# Singleton-style instance
settings = Settings()