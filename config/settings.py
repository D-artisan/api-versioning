from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Versioned API Example"
    debug: bool = True
    version_v1_prefix: str = "/v1"
    version_v2_prefix: str = "/v2"

    class Config:
        env_file = ".env"

settings = Settings()