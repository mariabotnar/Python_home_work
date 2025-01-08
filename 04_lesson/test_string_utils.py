from string_utils import StringUtils

import pytest

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
])

def test_trim_positive(input_string, output_string):
    string_utils = StringUtils()
    assert string_utils.trim(input_string) == output_string

# Принимает на вход текст с разделителем и возвращает список строк.

@pytest.mark.parametrize(('input_string', 'delimiter', 'output_string'), [
    ('Moscow,Paris,London', ',', ['Moscow', 'Paris', 'London']),
    ('1,2,3,4,5', ',', ['1', '2', '3', '4', '5']),
])

def test_to_list_positive(input_string, delimiter, output_string):
    string_utils = StringUtils()
    assert string_utils.to_list(input_string, delimiter) == output_string

# Возвращает `True`, если строка содержит искомый символ и `False` - если нет.

@pytest.mark.parametrize(('input_text', 'symbol'), [
    ('doll', 'o'),
    ('teddy-bear', '-'),
    ('Temperature -32', '3'),
    ('lesson 1', '2'),
])

def test_contains_positive(input_text, symbol):
    print(f'Проверяемая строка: {input_text}')
    print(f'Искомый символ: {symbol}')
    result = symbol in input_text
    print(f'Результат проверки: {result}')
    assert result

# Удаляет все подстроки из переданной строки.

@pytest.mark.parametrize(('input_string', 'char_to_remove', 'expected_output'), [
     ('daddy', 'd', 'ay'),
     ('mammy', 'y', 'mamm'),
     ('family-look', '-', 'familylook'),
])

def test_positive_delete_symbol(input_string, char_to_remove, expected_output):
     input_string = StringUtils()
     assert input_string.delete_symbol(char_to_remove, expected_output)

# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет.

@pytest.mark.parametrize(('input_text', 'symbol'), [
    ('doll', 'd'),
    ('teddy-bear', 't'),
    ('42', '4'),
    ('lesson 1', 'e'),
])

def test_start_with_positive(input_text, symbol):
    print(f'Строка для обработки: {input_text}')
    print(f'Искомый символ: {symbol}')
    result = symbol in input_text
    print(f'Результат проверки: {result}')
    assert result

# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет.

@pytest.mark.parametrize(('input_text', 'symbol'), [
    ('doll', 'd'),
    ('teddy-bear', 'r'),
    ('42', '2'),
    ('lesson 1', '1'),
])

def test_end_with_positive(input_text, symbol):
    print(f'Строка для обработки: {input_text}')
    print(f'Искомый символ: {symbol}')
    result = symbol in input_text
    print(f'Результат проверки: {result}')
    assert result

# Возвращает `True`, если строка пустая и `False` - если нет.

# Преобразует список элементов в строку с указанным разделителем.

# ПРОШУ ДОПОЛНИТЕЛЬНО ОБЪЯСНИТЬ АЛГОРРИТМ РАБОТЫ ОПЕРАТОРА BOOL.