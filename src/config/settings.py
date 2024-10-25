from pydantic_settings import BaseSettings

from functools import lru_cache

class Settings(BaseSettings):
    drivername : str
    username : str
    password : str
    host : str
    database : str
    port : int
    sqlalchemy_database_url = str
    
    class Config:
        env_file = ".env"

settings = Settings()

@lru_cache()
def get_settings():
    return settings