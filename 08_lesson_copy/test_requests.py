import requests


base_url = "https://x-clients-be.onrender.com"

# гет запрос работа со списком
def test_simple_req():
    resp = requests.get(base_url + '/company')

    response_body = resp.json()
    first_company = response_body[0]

    assert first_company["name"] == "Барбершоп 'ЦирюльникЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"

# пост запрос авторизация
def test_auth():
    creds = {
        'username': 'harrypotter',
        'password': 'expelliarmus'
    }

    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()["userToken"]
    assert resp.status_code == 201

# пост запрос создание компании
def test_create_company():
    creds = {
        'username': 'harrypotter',
        'password': 'expelliarmus'
    }

    company = {
        'name': 'python',
        'description': 'requests'
    }
    # авторизация
    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()['userToken']

    # создание
    my_headers = {}
    my_headers['x-client-token'] = token

    resp = requests.post(base_url + '/company', json=company, headers=my_headers)
    assert resp.status_code == 201