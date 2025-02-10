import json


# JSON
# JSON-текст, который по структуре похож на словарь
# обращаем внимание на кавычки
company_json = """
{
    "id": 111,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Барбершоп 'Цирюльникъ'",
    "description": "Крутые стрижки для крутых шишек"
    }
"""

# тест на проверку значения ключа
def test_parse_json():
    company = json.loads(company_json)
    assert company["id"] == 111
    # load - файл, loads - текст

# список объектов (массив) в формате json
company_list_json = """
[
    {
    "id": 111,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Барбершоп 'Цирюльникъ'",
    "description": "Крутые стрижки для крутых шишек"
    },
    {
    "id": 112,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Кондитерская Профи-троли",
    "description": "Сладко и точка"
    },
    {
    "id": 113,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Муж на час",
    "description": "Помощь в делах"
    }
]
"""

# тест на проверку значения ключа
def test_parse_array_json():
    company_list = json.loads(company_list_json)
    first_company = company_list[0]
    assert first_company["name"] == "Барбершоп 'Цирюльникъ'"
    # assert company_list[1]["id"] == 112


