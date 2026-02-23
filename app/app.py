from fastapi import FastAPI
from app.models import User, AgedUser, Feedback

app = FastAPI()

me = User(name = "Berg Ksenia", id= 1)

feedbacks = []

@app.get('/users')
def get_user():
    return me

@app.post('/user')
def set_adult(user: AgedUser):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

@app.post('/feedback')
def post_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}
