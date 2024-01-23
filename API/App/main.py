from random import randrange
from fastapi import FastAPI
from fastapi import Response, status, HTTPException,Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models_api,Schemas,utils
from .database import engine,get_db
from App.Schemas import UserCreate
from .routers import post,user,auth

models_api.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
                                password='password123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as error:
        print("Connection to database failed! ")
        print("Error: ", error)
        time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "welcome to API !"}


