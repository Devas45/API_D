from App import Schemas
import pytest

def test_get_all_posts(authorized_client,test_posts):
    res = authorized_client.get("/posts/")
    def validate(post):
        return Schemas.PostOut(**post)
    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    # print(list(posts_map))
    # print(res.json())

    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    # assert posts_list[0].Post.id == test_posts[0].id

def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts/")
    assert res.status_code == 401


def test_unauthorized_user_get_one_posts(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/8888")
    assert res.status_code == 404

def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    print(res.json())
    # post = Schemas.PostOut(**res.json())
    # assert post.Post.id == test_posts[0].id
    # assert post.Post.content == test_posts[0].content
    # assert post.Post.title == test_posts[0].title
    assert res.status_code == 200





@pytest.mark.parametrize("title,content,published",[
    ("awesome new title","awesome new content",True),
    ("afavourite Pizza","new Content one",False), 
    ("Browser","Mozilla",True),                                              
    ])
def test_create_post(authorized_client,test_posts,test_user,title,content,published):
    res = authorized_client.post("/posts/",json={"title":title, "content":content, "published":published})
    created_post = Schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user['id']


def test_create_post_default_published_true(authorized_client,test_user,test_posts):
    res = authorized_client.post("/posts/",json={"title":"arbitary_title", "content":"arbitary_content"})
    
    created_post = Schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == "arbitary_title"
    assert created_post.content == "arbitary_content"
    assert created_post.published == True
    assert created_post.owner_id == test_user['id']


def test_unauthorized_user_create_post(client, test_posts,test_user):
    res = client.post("/posts/",json = {"title":"arbitary_title","content":"arbitary_content"})
    assert res.status_code == 401








def test_unauthorized_user_delete_post(client, test_posts,test_user):
    res = client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401


def test_delete_post_success(client, test_posts,authorized_client):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 204

def test_delete_post_non_exist(client,test_posts,authorized_client):
    res = authorized_client.delete(f"/posts/800000")
    assert res.status_code == 404

def delete_other_user_posts(client,test_posts,authorized_client):
    res = authorized_client.delete(f"/posts/{test_posts[3].id}")
    assert res.status_code == 403







def test_update_post(authorized_client,test_posts,test_user):
    data = {
        "title":"Fourth Title",
        "content":"4th Content",
        "owner_id" : test_user['id'] 
    }
    res = authorized_client.put(f"/posts/{test_posts[0].id}",json = data)
    # print(res.json())
    updated_post = Schemas.Post(**res.json())
    assert res.status_code == 200
    assert updated_post.title == data['title']


def test_update_other_user_post(authorized_client,test_posts,test_user,test_user2):
    data = {
        "title":"Fourth Title",
        "content":"4th Content",
        "id": test_posts[3].id 
    }
    res = authorized_client.put(f"/posts/{test_posts[3].id}",json = data)
    assert res.status_code == 403


def test_unauthorized_user_update_post(client, test_posts,test_user):
    res = client.put(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_delete_post_non_exist(client,test_posts,authorized_client):
    data = {
        "title":"Fourth Title",
        "content":"4th Content",
        "id": test_posts[3].id 
    }
    res = authorized_client.put(f"/posts/800000",json = data)
    assert res.status_code == 404
