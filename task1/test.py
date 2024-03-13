import subprocess
import pytest

INTERPRETER = 'python'


def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()


test_data = {
    'anagram': [
        (['listen', 'silent'], ['YES']),
        (['hello', 'world'], ['NO']),
        (['abc', 'cbaa'], ['NO'])
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50']),
        (['-4', '0'], ['-4', '-4', '0'])
    ],
    'division': [
        (['1', '2'], ['0', '0.5']),
        (['10', '5'], ['2', '2.0']),
        (['-4', '0'], ['devision by zero'])
    ],
    'happiness': [
        (['3 2', '1 5 3', '3 1', '5 7'], ['1']),
        (['6 2', '1 2 3 4 5 6', '1 3 5', '2 4'], ['1']),
        (['3 3', '1 2 3', '1 2 3', '4 5 6'], ['3'])
    ],
    'is_leap': [
        (['2000'], ['True']),
        (['1900'], ['False']),
        (['2024'], ['True']),
    ],
    'lists': [
        (['4', 'append 1', 'append 2', 'insert 1 3', 'print'], ['[1, 3, 2]']),
        (['5', 'append 4', 'insert 0 5', 'insert 2 6', 'print', 'remove 5'], ['[5, 4, 6]']),
        (['3', 'insert 0 3', 'insert 0 2', 'print'], ['[2, 3]'])
    ],
    'loops': [
        (['10'], ['0', '1', '4', '9', '16', '25', '36', '49', '64', '81']),
        (['5'], ['0', '1', '4', '9', '16']),
        (['20'],
         ['0', '1', '4', '9', '16', '25', '36', '49', '64', '81', '100', '121', '144', '169', '196', '225', '256',
          '289', '324', '361']),

    ],
    'matrix_mult': [
        (['3', '1 2 3', '4 5 6', '7 8 9', '9 8 7', '6 5 4', '3 2 1'], ['30 24 18', '84 69 54', '138 114 90']),
        (['2', '1 0', '0 1', '1 2', '3 4'], ['1 2', '3 4']),
        (['4', '1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 16', '1 0 0 0', '0 1 0 0', '0 0 1 0', '0 0 0 1'],
         ['1 2 3 4', '5 6 7 8', '9 10 11 12', '13 14 15 16']),
    ],
    'metro': [
        (['5', '1 5', '2 4', '1 3', '4 5', '1 8', '4'], ['4']),
        (['7', '1 1', '6 9', '2 6', '3 5', '2 4', '5 6', '2 9', '5'], ['4']),
        (['6', '1 6', '3 7', '4 6', '3 5', '6 7', '3 10', '6'], ['5'])
    ],
    'minion_game': [
        (['BANANA'], ['Stuart 12']),
        (['HELLO'], ['Stuart 10']),
        (['AEIOU'], ['Kewin 15'])
    ],
    'nested_list': [
        (['5', 'Harry', '37.21', 'Berry', '37.21', 'Tina', '37.2', 'Akriti', '41', 'Harsh', '39'], ['Berry', 'Harry']),
        (['3', 'Andrey', '55', 'Vasily', '60', 'Ivan', '60'], ['Ivan', 'Vasily']),
        (['2', 'Alexey', '50', 'Dmitriy', '55'], ['Dmitriy'])
    ],
    'pirate_ship': [
        (['20 4', 'apple 2 34', 'board 5 54', 'circle 98 7', 'drop 7 7'],
         ['board 5 54', 'apple 2 34', 'circle 13 0.93']),
        (['20 6', 'a 2 2', 'b 3 3', 'c 4 4', 'd 5 6', 'e 7 7', 'n 8 8'], ['n 8 8', 'e 7 7', 'd 5 6', 'c 0 0.0']),
        (['4 4', 'a 1 1', 'b 2 2', 'c 3 3', 'd 4 4'], ['d 4 4', 'c 0 0.0']),
        (['10 10', 'q 1 1', 'w 2 2', 'f 45 6', 'g 34 2', 'h 6 7', 'e 45 6', 'l 9 0', 'b 8 9', 'v 4 6', 'm 9 3'],
         ['b 8 9', 'h 2 2.33'])
    ],
    'print_function': [
        (['6'], ['123456']),
        (['9'], ['123456789']),
        (['4'], ['1234']),
        (['20'], ['1234567891011121314151617181920']),
        (['1'], ['1']),
        (['7'], ['1234567']),
    ],
    'python_if_else': [
        ('1', 'Weird'),
        ('4', 'Not Weird'),
        ('3', 'Weird'),
        ('6', 'Weird'),
        ('22', 'Not Weird')
    ],
    'second_score': [
        (['6', '1 2 3 4 5 6'], ['5']),
        (['7', '10 20 30 40 50 60 70'], ['60']),
        (['11', '5 10 15 20 25 30 35 40 40 40'], ['35']),
        (['4', '0 3 6 9'], ['6']),
        (['10', '2 4 6 8 10 12 14 16 14 14'], ['14'])
    ],
    'split_and_join': [
        (['test string'], ['test-string']),
        (['hello world'], ['hello-world']),
        (['python programming'], ['python-programming']),
        (['open ai'], ['open-ai']),
        (['data science is fun'], ['data-science-is-fun'])
    ],
    'swap_case': [
        (['hello world'], ['HELLO WORLD']),
        (['Pythonist 2'], ['pYTHONIST 2']),
        (['Natural Language Processing'], ['nATURAL lANGUAGE pROCESSING']),
        (['Www.MosPolytech.ru'], ['wWW.mOSpOLYTECH.RU']),
        (['Cybersecurity Measures '], ['cYBERSECURITY mEASURES'])
    ]
}


def test_hello_world():
    assert run_script('hello_world.py') == 'Hello, world!'


@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', [input_data]) == expected


@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    assert run_script('division.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data).split('\n') == expected


def test_hello():
    assert run_script('hello.py') == 'Hello World'


@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data).split('\n') == expected


#

@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data).split('\n') == expected


#

@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data).split('\n') == expected


@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data).split('\n') == expected
