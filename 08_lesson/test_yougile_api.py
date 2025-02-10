import pytest
import json
import requests



# переменная для url
base_url = 'https://ru.yougile.com/api-v2/'
# переменная для token
my_token = 'NOtSMkYh8+8qSwtSZSfQfVtwu8y7d7ZYI6gzLAWOl1PLMjGkJvsu9HVYSnxudRzj'
# переменная для заголовка
headers = {
    'Authorization': f'bearer {my_token}',
    'Content-Type': 'application/json'
}

# фикстура для создания нового проекта
@pytest.fixture()
def create_project():
    project_data = {
        'title': 'Мой проект'
    }
    response = requests.post(base_url + 'projects', json=project_data, headers=headers)
    assert response.status_code == 201
    project_id = response.json()['id']
    yield project_id

# POST создать проект позитив
def test_create_project_positive():
    project_data = {
        'title': 'Мой проект'
    }
    response = requests.post(base_url + 'projects', json=project_data, headers=headers)
    assert response.status_code == 201
    assert 'id' in response.json()

# POST создать проект негатив
def test_create_project_negative():
    project_data = {
        'title': ''
    }
    response = requests.post(base_url + 'projects', json=project_data, headers=headers)
    assert response.status_code == 400

# GET получить список проектов позитив
def test_get_project_positive():
    response = requests.get(base_url + 'projects', headers=headers)
    assert response.status_code == 200
    assert "content" in response.json()
    assert isinstance(response.json()["content"], list)

# GET получить проект по id позитив
def test_get_project_id_positive(create_project):
    project_id = create_project
    response = requests.get(base_url + f'projects/{project_id}', headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == project_id
    assert "id" in response.json()

# PUT изменить название проекта позитив
def test_update_project_positive(create_project):
    project_id = create_project
    update_data = {
        'title': 'Мой новый проект'
    }
    response = requests.put(base_url + f'projects/{project_id}', headers=headers)
    assert response.status_code == 200
    assert "id" in response.json()

# PUT изменить название проекта негатив
def test_update_project_negative(create_project):
    project_id = create_project
    update_data = {
        'title': '   '
    }
    response = requests.put(base_url + f'projects/{project_id}', headers=headers)
    assert response.status_code == 404