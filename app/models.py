from pydantic import BaseModel, Field, field_validator

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
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator('message')
    @classmethod
    def validate_message(cls, v: str) -> str:
        bad_words = ['кринж', 'рофл', 'вайб']
        v_lower = v.lower()
        for word in bad_words:
            if word in v_lower:
                raise ValueError('Использование недопустимых слов')
        return v
