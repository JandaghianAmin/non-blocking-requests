from fastapi import FastAPI
import string
import random

app = FastAPI()

@app.get("/")
async def index():
    mystr =''.join(random.choices(string.ascii_lowercase,k=15))
    return {'data':mystr}
    

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}