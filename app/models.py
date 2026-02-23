from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int

class AgedUser(BaseModel):
    name: str
    age: int

class AgedUserResponse(BaseModel):
    name: str
    age: int
    is_adult: bool

class Feedback(BaseModel):
    name: str
    message: str