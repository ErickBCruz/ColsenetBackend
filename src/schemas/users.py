from pydantic import BaseModel
from datetime import datetime

class CreateUserDTO(BaseModel):
    username = str
    email = str
    password = str