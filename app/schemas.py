from pydantic import BaseModel,EmailStr, conint
from datetime import datetime
from typing import Optional
from pydantic.types import conint



class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)



class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes = True
     
class BasePost(BaseModel):
    title: str
    content: str
    published: bool = True
    
class PostCreate(BasePost):
    pass

class PostResponse(BasePost):
    id: int
    created_at: datetime
    user_id: int
    user: UserResponse
    
    class Config:
        from_attributes = True
        
class PostOut(BaseModel):
    Post: PostResponse
    votes: int
    
    class Config:
        from_attributes = True
        
class User(BaseModel):
    email: EmailStr
    password: str

   
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    user_id: Optional[int] = None