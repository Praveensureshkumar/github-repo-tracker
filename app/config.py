from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    GITHUB_API_URL: str = "https://api.github.com"

    class Config:
        env_file = ".env"

settings = Settings()
