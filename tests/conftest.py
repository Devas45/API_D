from fastapi.testclient import TestClient
from App.main import app
from App import Schemas
from App.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from App.database import get_db,Base
from App.oauth2 import create_access_token
import pytest
from App import models_api
from .database import client,session

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password123@localhost:5432/fastapi_test'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Testing_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base.metadata.create_all(bind=engine)
# Base = declarative_base()

# Dependency
# def override_get_db():
#     db = Testing_SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# app.dependency_overrides[get_db] = override_get_db
# client = TestClient(app)

# @pytest.fixture(scope="module")
@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    #run thee code before the TestClient runs
    Base.metadata.create_all(bind=engine)
    # yield TestClient(app)
    #run thee code after the TestClient runs
    # Base.metadata.drop_all(bind=engine).
    db = Testing_SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

@pytest.fixture    
def test_user2(client):
    user_data = {"email":"gee@gmail.com","password":"password123"}
    res = client.post("/users/",json=user_data) 
    assert res.status_code == 201
    # print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture    
def test_user(client):
    user_data = {"email":"geek@gmail.com","password":"password123"}
    res = client.post("/users/",json=user_data) 
    assert res.status_code == 201
    # print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({"user_id":test_user['id']})

@pytest.fixture
def authorized_client(client,token):
    client.headers = {
        **client.headers,
        "Authorization":f"Bearer {token}"
    }
    return client

@pytest.fixture
def test_posts(test_user,session,test_user2):
    posts_data = [{
        "title":"first Title",
        "content":"1st Content",
        "owner_id" : test_user['id'] 
    },{
        "title":"second Title",
        "content":"2nd Content",
        "owner_id" : test_user['id'] 
    },{
        "title":"Third Title",
        "content":"3rd Content",
        "owner_id" : test_user['id'] 
    },
    {
        "title":"Third Title",
        "content":"3rd Content",
        "owner_id" : test_user2['id'] 
    }]
    
    def func(post):
        return models_api.Post(**post)

    post_map = map(func,posts_data)
    posts = list(post_map)
    session.add_all(posts)

    session.add_all([models_api.Post(title = "first Title", content = "1st Content",owner_id = test_user['id']),
                     models_api.Post(title = "second Title", content = "2nd Content",owner_id = test_user['id']),
                     models_api.Post(title = "Third Title", content = "3rd Content",owner_id = test_user['id'])])

    session.commit()
    posts = session.query(models_api.Post).all()
    return posts

