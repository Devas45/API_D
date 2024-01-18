from datetime import datetime
from pydantic import BaseModel,EmailStr

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     # rating: Optional[int] = None

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# extend child to parent
class PostCreate(PostBase):
    pass

class Post(BaseModel):
    id:int
    content: str
    published: bool 
    created_at: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email:EmailStr
    password:str

