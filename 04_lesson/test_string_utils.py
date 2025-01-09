import pytest
from string_utils import StringUtils


# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст.

@pytest.mark.parametrize(('input_string', 'output_string'), [
    ('lesson', 'Lesson'),
    ('LESSON', 'Lesson'),
    ('Lesson', 'Lesson'),
    ('мАрия', 'Мария'),
    ('б', 'Б')
])
def test_capitalize_positive(input_string, output_string):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_string) == output_string


@pytest.mark.parametrize(('input_string', 'output_string'), [
    ('', ''),
    ('4', '4'),
    ('...', '...'),
])
def test_capitalize_negative(input_string, output_string):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_string) == output_string


# Принимает на вход текст и удаляет пробелы в начале, если они есть.

@pytest.mark.parametrize(('input_string', 'output_string'), [
    (' Anna', 'Anna'),
    ('     New year', 'New year'),
    ('     ', ''),
])
def test_trim_positive(input_string, output_string):
    string_utils = StringUtils()
    assert string_utils.trim(input_string) == output_string


# Принимает на вход текст с разделителем и возвращает список строк.

@pytest.mark.parametrize(('input_string', 'delimiter', 'output_string'), [
    ('Moscow,Paris,London', ',', ['Moscow', 'Paris', 'London']),
    ('1,2,3,4,5', ',', ['1', '2', '3', '4', '5']),
    ('a-b,b-c,c-d', ',', ['a-b', 'b-c', 'c-d']),
])
def test_to_list_positive(input_string, delimiter, output_string):
    string_utils = StringUtils()
    assert string_utils.to_list(input_string, delimiter) == output_string


# Возвращает `True`, если строка содержит искомый символ и `False` - если нет.

@pytest.mark.parametrize(('input_text', 'symbol'), [
    ('doll', 'o'),
    ('teddy-bear', '-'),
    ('Temperature -32', '-32'),
    ('lesson 1', '1'),
])
def test_contains_positive(input_text, symbol):
    string_utils = StringUtils()
    assert string_utils.contains(input_text, symbol)


# Удаляет все подстроки из переданной строки.

@pytest.mark.parametrize(('input_string', 'char_to_remove', 'expected_output'), [
     ('daddy', 'd', 'ay'),
     ('mammy', 'y', 'mamm'),
     ('family-look', '-', 'familylook'),
     ('skypro', 'pro', 'sky'),
])
def test_positive_delete_symbol(input_string, char_to_remove, expected_output):
     input_string = StringUtils()
     assert input_string.delete_symbol(char_to_remove, expected_output)


# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет.

@pytest.mark.parametrize(('input_text', 'symbol'), [
    ('doll', 'd'),
    ('teddy-bear', 't'),
    ('42', '4'),
    ('Lesson 1', 'L'),
])
def test_start_with_positive(input_text, symbol):
    input_string = StringUtils()
    assert input_string.starts_with(input_text, symbol) is True

@pytest.mark.parametrize(('input_text', 'symbol'), [
    ('doll', 'D'),
    ('teddy-bear', 'e'),
    ('42', ' '),
    ('Lesson 1', '1'),
])
def test_start_with_negative(input_text, symbol):
    input_string = StringUtils()
    assert input_string.starts_with(input_text, symbol) is False


# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет.

@pytest.mark.parametrize(('input_text', 'symbol'), [
    ('doll', 'l'),
    ('teddy-bear', 'r'),
    ('42', '2'),
    ('lesson 1', '1'),
])
def test_end_with_positive(input_text, symbol):
    input_string = StringUtils()
    assert input_string.end_with(input_text, symbol) is True

@pytest.mark.parametrize(('input_text', 'symbol'), [
    ('doll', 'u'),
    ('teddy-bear', '-'),
    ('42', '4'),
    ('lesson 1', 'n'),
])
def test_end_with_negative(input_text, symbol):
    input_string = StringUtils()
    assert input_string.end_with(input_text, symbol) is False


# Возвращает `True`, если строка пустая и `False` - если нет.

@pytest.mark.parametrize(('input_text'), [
    (''),
    (' '),
])
def test_is_empty_positive(input_text):
    input_string = StringUtils()
    assert input_string.is_empty(input_text) is True

@pytest.mark.parametrize(('input_text'), [
    ('1234'),
    (' - '),
])
def test_is_empty_negative(input_text):
    input_string = StringUtils()
    assert input_string.is_empty(input_text) is False


# Преобразует список элементов в строку с указанным разделителем.

@pytest.mark.parametrize(('input_list', 'delimiter', 'output_string'), [
    (['Moscow', 'Paris', 'London'], ',', 'Moscow,Paris,London'),
    (['1', '2', '3', '4', '5'], ',', '1,2,3,4,5'),
    (['a', 'b', 'c'], ':', 'a:b:c'),
])
def test_list_to_string_positive(input_list, delimiter, output_string):
    string_utils = StringUtils()
    assert string_utils.list_to_string(input_list, delimiter) == output_string