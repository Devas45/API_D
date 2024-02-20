from fastapi import Response, status, HTTPException,Depends,APIRouter
from .. import Schemas,database,models_api,oauth2
from ..database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix = "/vote",
    tags=['Vote']
)


@router.post("/",status_code = status.HTTP_201_CREATED)
def vote(vote:Schemas.Vote,db:Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):

    post = db.query(models_api.Post).filter(models_api.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Post with id: {vote.post_id} does not exist")
    
    vote_query = db.query(models_api.Vote).filter(models_api.Vote.post_id == vote.post_id,models_api.Vote.user_id == current_user.id)
    found_vote = vote_query.first()

    if(vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"user {current_user.id} has already voted on post {vote.post_id}")
        new_vote = models_api.Vote(post_id=vote.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"succesfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = "Vote does not exist")
        
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"meassge":"succesfully deleted vote"}