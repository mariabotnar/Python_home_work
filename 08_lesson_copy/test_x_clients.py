# тест на получение списка компаний
import requests
import json


# переменная для корректности передачи
base_url = "https://x-clients-be.onrender.com"

# получение списка компаний
def test_get_companies():
    # переходим на страницу
    resp = requests.get(base_url + '/company')
    # сохраняем ответ в нужном формате
    body = resp.json()

    # проверяем статус запроса
    assert resp.status_code == 200
    # проверяем, что список не равен 0
    assert len(body) > 0
    # как проверить, сколько у нас компаний будет - ВОПРОС ОТКРЫТ

# список активных компаний
# проверка работы фильтров
def test_get_active_companies():
    # получаем список всех компаний
    resp = requests.get(base_url + '/company')
    full_list = resp.json()
    # получаем список активных компаний
    my_params = {'active': 'true'}
    resp = requests.get(base_url + '/company', params=my_params)
    filtered_list = resp.json()
    # проверяем, что список 1 > списка 2
    assert len(full_list) > len(filtered_list)

# набор параметров можно передавать через словарь, ключ - значение
#
#
# добавление новой компании
# def test_add_new():
    # получаем количество компаний до создания
    # создаём новую компанию
    # снова получаем количество компаний
    # проверяем, что стало + 1
    # проверяем название и описание последней компании
    # проверяем, что id последней компании из списка равен ответу из шага 2
