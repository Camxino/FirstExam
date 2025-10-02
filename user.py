from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    username: str
    password: str
    email: Optional[str] = None
    is_active: bool = True