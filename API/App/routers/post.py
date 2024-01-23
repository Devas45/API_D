from fastapi import Response, status, HTTPException,Depends,APIRouter
from typing import Optional,List
from sqlalchemy.orm import Session
from .. import Schemas,models_api,oauth2
from ..database import get_db

router = APIRouter(
    prefix = "/posts",
    tags=['Posts']
)

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

@router.get("/sqlalchemy")
def test_posts(db:Session = Depends(get_db)):
    posts = db.query(models_api.Post).all()
    print(posts)
    return {"data" : posts}

@router.get("/",response_model=List[Schemas.Post])
def get_post(db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    posts = db.query(models_api.Post).all()
    print(posts)
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=Schemas.Post)
def create_posts(post: Schemas.PostCreate,db:Session = Depends(get_db),
                current_user:int = Depends(oauth2.get_current_user)):
    
    # cursor.execute("""INSERT INTO posts (post_title,post_content,published) VALUES (%s,%s,%s) RETURNING * """,
    #                (post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # # we need to commit
    # conn.commit()
    print(current_user.email)
    new_post = models_api.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
# new_post is a SQLALCHEMY MODEL,not a dict()


@router.get("/{id}",response_model=Schemas.Post)
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

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: str,db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE post_id = %s RETURNING *""",(str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    # idx = find_idx_post(id)
    # if idx is None:
    deleted_post = db.query(models_api.Post).filter(models_api.Post.id == id).first()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} doesn't exist")
    
    db.delete(deleted_post)
    db.commit()
    # my_posts.pop(idx)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=Schemas.Post)
def update_post(id: int, up_post: Schemas.PostCreate,db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
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
    # return u_post
    return updated_post.first()