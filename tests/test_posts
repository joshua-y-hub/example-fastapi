from typing import List
from app import schemas



def test_get_all_posts(authorized_client,test_posts):
    res = authorized_client.get("/posts/")
    posts = schemas.PostOut(**res.json()[0])
    assert res.status_code == 200