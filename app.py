import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return "Hello world" 
 

if __name__ == "__main__":  
    uvicorn.run(app, host="0.0.0.0", port=8000)