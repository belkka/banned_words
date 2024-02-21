import random

import fastapi


app = fastapi.FastAPI()


@app.get("/", response_class=fastapi.responses.PlainTextResponse)
async def root():
    roll = random.randint(1, 20)
    return (
        f"Hello world. Your random number is {roll}."
    )
