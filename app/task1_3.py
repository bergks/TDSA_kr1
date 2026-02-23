from fastapi import FastAPI

app = FastAPI()

@app.post('/calculate')
def sum_num(num1: int, num2: int):
    return {'result': f'{num1+num2}'}