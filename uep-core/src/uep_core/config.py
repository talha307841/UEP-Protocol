from pydantic import BaseSettings

class Settings(BaseSettings):
    # General settings
    app_name: str = "Universal Exchange Protocol"
    version: str = "1.0.0"
    
    # Server settings
    server_host: str = "0.0.0.0"
    server_port: int = 50051
    
    # Logging settings
    log_level: str = "INFO"
    
    # Other configurations can be added here

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()