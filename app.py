import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return "Hello world" 
 