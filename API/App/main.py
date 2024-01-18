from random import randrange
from typing import Optional,List
from fastapi import FastAPI
from fastapi import Response, status, HTTPException,Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models_api,Schemas
from .database import engine,get_db
from App.Schemas import UserCreate

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

my_posts = [{"title": "Title of post 1", "content": "content of post 1", "id": 1},
            {"title": "Favourite Foods", "content": "PIZZZZZZZZZA", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_idx_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
async def root():
    return {"message": "welcome to API !"}

@app.get("/sqlalchemy")
def test_posts(db:Session = Depends(get_db)):
    posts = db.query(models_api.Post).all()
    print(posts)
    return {"data" : posts}

@app.get("/posts",response_model=List[Schemas.Post])
def get_post(db:Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models_api.Post).all()
    print(posts)
    return posts

@app.post("/posts", status_code=status.HTTP_201_CREATED,response_model=Schemas.Post)
def create_posts(post: Schemas.PostCreate,db:Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (post_title,post_content,published) VALUES (%s,%s,%s) RETURNING * """,
    #                (post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # # we need to commit
    # conn.commit()
    new_post = models_api.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
# new_post is a SQLALCHEMY MODEL,not a dict()


@app.get("/posts/{id}",response_model=Schemas.Post)
def get_post(id: str,db:Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE post_id = %s """,(str(id)))
    # test_post = cursor.fetchone()
    # print(post)
    # post = find_post(id)
    # post = find_post(id)
    test_post = db.query(models_api.Post).filter(models_api.Post.id == id).first()
    print(test_post)
    if not test_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return test_post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: str,db:Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE post_id = %s RETURNING *""",(str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    # idx = find_idx_post(id)
    # if idx is None:
    deleted_post = db.query(models_api.Post).filter(models_api.Post.id == id).first()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} doesn't exist")
    
    deleted_post.delete(synchronize_session = False)
    db.commit()
    # my_posts.pop(idx)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}",response_model=Schemas.Post)
def update_post(id: int, up_post: Schemas.PostCreate,db:Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET post_title = %s,post_content = %s,published = %s WHERE post_id = %s RETURNING *""",
    #                (post.title,post.content,post.published,str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
      # idx = find_idx_post(id)
    updated_post = db.query(models_api.Post).filter(models_api.Post.id == id)
    u_post = updated_post.first()

    if u_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} doesn't exist")
    
    updated_post.update(up_post.dict(),synchronize_session = False)
    db.commit()
    # post_dict = post.model_dump()
    # post_dict['id'] = id
    # my_posts[idx] = post_dict
    # return u_post_check it
    return updated_post.first()

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: Schemas.UserCreate,db:Session = Depends(get_db)):
    new_user = models_api.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user