from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World"

@app.get("/json")
def getJson():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# 실행은 해당 위치에서 터미널로 실행
# uvicorn main:app --reload