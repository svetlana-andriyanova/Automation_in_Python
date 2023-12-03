import pytest
import requests
import yaml

with open('config.yaml') as f:
    conf = yaml.safe_load(f)
    url = conf["url"]
    login = conf["login"]
    password = conf["password"]
    url_get = conf["url_get"]
    url_post = conf["url_post"]
    title = conf["title"]
    description = conf["description"]
    content = conf["content"]

def test_get_token(get_token):
    response = requests.post(url=url,
                             data={"username": login, "password": password})
    res_token = response.json()["token"]
    assert response.status_code == 200
    assert res_token == get_token


def test_check_post(get_token, request_get):
    headers = {'X-Auth-Token': get_token}
    response = requests.get(url_get, headers=headers,
                            params={'owner': 'notMe'})
    posts = response.json()
    assert response.status_code == 200
    assert posts == request_get


def test_check_title(get_token):
    headers = {'X-Auth-Token': get_token}
    response = requests.post(url=url_post, headers=headers,
                             params={"title": title,
                                     "description": description,
                                     "content": content})
    title_post = response.json()["title"]
    assert response.status_code == 200
    assert title_post == title


def test_check_post_2(get_token, request_post):
    headers = {'X-Auth-Token': get_token}
    response = requests.get(url_get, headers=headers, params={'owner': 'Me'})
    posts = response.json()
    assert response.status_code == 200
    assert any(post["title"] == request_post for post in posts["data"])


if __name__ == "__main__":
    pytest.main(['-vv'])