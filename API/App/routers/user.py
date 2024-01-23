from fastapi import Response, status, HTTPException,Depends,APIRouter
from .. import Schemas,models_api,utils
from ..database import engine,get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/users", status_code=status.HTTP_201_CREATED,response_model=Schemas.UserOut)
def create_user(user: Schemas.UserCreate,db:Session = Depends(get_db)):
    
    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models_api.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/users/{id}',response_model = Schemas.UserOut)
def get_user(id:int ,db: Session = Depends(get_db)):
    user_post = db.query(models_api.User).filter(models_api.User.id == id).first()
    if not user_post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, message = f"User not found with id:{id}")
    
    return user_post


# routers - split the path operations, users and posts