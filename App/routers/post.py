from fastapi import Response, status, HTTPException,Depends,APIRouter
from typing import Optional,List
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .. import Schemas,models_api,oauth2
from ..database import get_db
from sqlalchemy import func
from sqlalchemy.orm import aliased
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix = "/posts",
    tags=['Posts']
)

# my_posts = [{"title": "Title of post 1", "content": "content of post 1", "id": 1},
#             {"title": "Favourite Foods", "content": "PIZZZZZZZZZA", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_idx_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i

@router.get("/sqlalchemy")
def test_posts(db:Session = Depends(get_db)):
    posts = db.query(models_api.Post).all()
    print(posts)
    return {"data" : posts}

@router.get("/", response_model=List[Schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # Use a subquery to count votes for each post
    subquery = (
        db.query(models_api.Post.id, func.count(models_api.Vote.post_id).label("votes"))
        .outerjoin(models_api.Vote, models_api.Vote.post_id == models_api.Post.id)
        .group_by(models_api.Post.id)
        .subquery()
    )

    # Join the posts with the subquery to get the vote counts
    results = (
        db.query(models_api.Post, subquery.c.votes)
        .outerjoin(subquery, models_api.Post.id == subquery.c.id)
        .filter(models_api.Post.title.contains(search))
        .limit(limit)
        .offset(skip)
        .all()
    )

    # Construct the response using PostOut instances
    formatted_results = [
        Schemas.PostOut(
            id=post[0].id,
            title=post[0].title,
            content=post[0].content,
            published=post[0].published,
            created_at=post[0].created_at,
            owner=Schemas.UserOut(**post[0].owner.__dict__),
            votes=post[1]
        )
        for post in results
    ]
    return formatted_results



@router.post("/", status_code=status.HTTP_201_CREATED,response_model=Schemas.Post)
def create_posts(post: Schemas.PostCreate,db:Session = Depends(get_db),
                current_user:int = Depends(oauth2.get_current_user)):
    
    # cursor.execute("""INSERT INTO posts (post_title,post_content,published) VALUES (%s,%s,%s) RETURNING * """,
    #                (post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # # we need to commit
    # conn.commit()
    print(current_user.email)
    print(current_user.id)
    new_post = models_api.Post(owner_id = current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
# new_post is a SQLALCHEMY MODEL,not a dict()


@router.get("/{id}",response_model=Schemas.Post)
def get_post(id: str,db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
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
    if test_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not Authorised to Perform requested action")
    
    return test_post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: str,db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE post_id = %s RETURNING *""",(str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    # idx = find_idx_post(id)
    # if idx is None:
    post_query = db.query(models_api.Post).filter(models_api.Post.id == id)
    deleted_post = post_query.first()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} doesn't exist")
    
    if deleted_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not Authorised to Perform requested action")

    post_query.delete(synchronize_session = False)
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
    
    if u_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not Authorised to Perform requested action")
    
    updated_post.update(up_post.dict(),synchronize_session = False)
    db.commit()
    # post_dict = post.model_dump()
    # post_dict['id'] = id
    # my_posts[idx] = post_dict
    # return u_post
    return updated_post.first()


# for spaces in query_parameters we use %



# @router.get("/", response_model=List[Schemas.PostOut])
# def get_post(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
#              Limit: int = 2, skip: int = 0, search: Optional[str] = ""):
#     # Query for posts matching the search criteria
#     posts = db.query(models_api.Post).filter(models_api.Post.title.contains(search)).limit(Limit).offset(skip).all()

#     # Create an alias for the Post model to use in the subquery
#     post_alias = aliased(models_api.Post)

#     # Subquery to count votes for each post
#     subquery = (
#         db.query(post_alias.id, func.count(models_api.Vote.post_id).label("votes"))
#         .outerjoin(models_api.Vote, models_api.Vote.post_id == post_alias.id)
#         .group_by(post_alias.id)
#         .subquery()
#     )

#     # Join the posts with the subquery to get the vote counts
#     results = (
#         db.query(models_api.Post, subquery.c.votes)
#         .outerjoin(subquery, models_api.Post.id == subquery.c.id)
#         .filter(models_api.Post.title.contains(search))
#         .limit(Limit)
#         .offset(skip)
#         .all()
#     )

#     # Construct the response using PostOut instances
#     formatted_results = [
#         Schemas.PostOut(post=Schemas.Post(**post.__dict__), votes=votes)
#         for post, votes in results
#     ]

#     return formatted_results