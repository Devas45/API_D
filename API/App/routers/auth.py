from fastapi import Response, status, HTTPException,Depends,APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import Schemas,models_api, oauth2,utils

router = APIRouter(tags=['Authentication'])

@router.post('/login',response_model=Schemas.Token)
def login(user_credentials:OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    
    # username,password - Outh2 doesnt care aboyut email or password,take it as username
    # {
    #     "username" : ""
    #     "password" : ""
    # }
    user_v = db.query(models_api.User).filter(models_api.User.email==user_credentials.username).first()
    if not user_v:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail = f"Invalid Credentials")
    if not utils.verify(user_credentials.password,user_v.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail = f"Invalid Credentials")
    
    # create a token
    # return a token
    access_token = oauth2.create_access_token(data={"user_id": user_v.id})
    return {"access_token": access_token, "token_type": "bearer"}
