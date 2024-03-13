import subprocess
import pytest

from fact import fact_it, fact_rec
from show_employee import show_employee
from sum_and_sub import sum_and_sub
from process_list import process_list, process_list_gen
from my_sum import my_sum
# from my_sum_argv import my_sum_argv
# from files_sort import files_sort
# from file_search import file_search
from email_validation import fun
from fibonacci import fibonacci, cube
from average_scores import compute_average_scores
from plane_angle import Point, plane_angle
from phone_number import wrapper
from people_sort import name_format
from complex_numbers import Complex
from circle_square_mk import circle_square_mk
from log_decorator import function_logger

INTERPRETER = 'python'


def run_script(filename, args, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename, *args],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()


test_data = {
    'fact_it': [
        (5, 120),
        (10, 3628800),
        (15, 1307674368000),
        (0, 1),
        (1, 1),
    ],
    'fact_rec': [
        (5, 120),
        (10, 3628800),
        (15, 1307674368000),
        (0, 1),
        (1, 1),
    ],
    'show_employee': [
        (('Vasya Pupkin', 1024), 'Vasya Pupkin: 1024 ₽'),
        (('Сергеев Сергей Сергеевич',), 'Сергеев Сергей Сергеевич: 100000 ₽'),
        (('a', 1), 'a: 1 ₽'),
    ],
    'sum_and_sub': [
        ((10, 20), (30, -10)),
        ((1, -5), (-4, 6)),
        ((0, -255), (-255, 255)),
        ((15, 15), (30, 0)),
    ],
    'process_list': [
        ([1, 2, 3, 4, 12, 34, 56, 78], [1, 4, 27, 16, 144, 1156, 3136, 6084]),
        ([-5, -4, -3, 1, 2, 0], [-125, 16, -27, 1, 4, 0]),
        ([-9, 3, 54, -12, 1], [-729, 27, 2916, 144, 1]),
        ([], [])
    ],
    'process_list_gen': [
        ([1, 2, 3, 4, 12, 34, 56, 78], [1, 4, 27, 16, 144, 1156, 3136, 6084]),
        ([-5, -4, -3, 1, 2, 0], [-125, 16, -27, 1, 4, 0]),
        ([-9, 3, 54, -12, 1], [-729, 27, 2916, 144, 1]),
        ([], [])
    ],
    'my_sum': [
        ((1, 2, 3, 4, 5), 15),
        ((10, -1000, 0), -990),
        ((1,), 1),
        ((), 0)
    ],
    'my_sum_argv': [
        (('1', '2', '3', '4', '5'), '15.0'),
        (('10', '-10', '0', '0', '-999'), '-999.0'),
        (('10', '-1000', '0'), '-990.0'),
        ((), '0')
    ],
    'files_sort': [
        (['.'], ['test.log\n', 'average_scores.py\n', 'circle_square_mk.py\n', 'complex_numbers.py\n',
               'email_validation.py\n', 'fact.py\n', 'fibonacci.py\n', 'file_search.py\n', 'files_sort.py\n',
               'log_decorator.py\n', 'my_sum.py\n', 'my_sum_argv.py\n', 'people_sort.py\n','phone_number.py\n',
               'plane_angle.py\n', 'process_list.py\n', 'show_employee.py\n', 'sum_and_sub.py\n', 'test.py\n',
               'task3.rar\n', 'hw2.zip\n'])
    ],
    'file_search': [
        ('my_sum.py', ('def my_sum(*args):\nreturn sum(args)')),
        ('fact.py',
            ('def fact_rec(n):\n', '    if n == 0:\n', '        return 1\n', '    else:\n', '        return n * fact_rec(n-1)')),
        ('nonexistent.file', ('File nonexistent.file not founded'))
    ],
    'email_validation': [
        ('lara@mospolytech.ru', True),
        ('brian-23@mospolytech.ru', True),
        ('britts_54@mospolytech.ru', True),
        ('bad email@mail.dotru', False)
    ],
    'fibonacci': [
        (14, [0, 1, 1, 8, 27, 125, 512, 2197, 9261, 39304, 166375, 704969, 2985984, 12649337]),
        (3, [0, 1, 1]),
        (5, [0, 1, 1, 8, 27]),
        (0, []),
        (1, [0])
    ],
    'average_scores': [
        (([[89, 90, 78, 93, 80], [90, 91, 85, 88, 86], [91, 92, 83, 89, 90.5]]),
         [90.0, 91.0, 82.0, 90.0, 85.5]),
        (([10, 11, 12], [6, 5, 4], [17, 8, 22]),
         [11.0, 8.0, 12.6]),
        (([[1]]), [1.0])
    ],
    'plane_angle': [
        ((Point(0, 0, 0), Point(0, 0, 10), Point(0, 19, 0), Point(0, 19, 10)), 180.0),
        ((Point(0, 0, 0), Point(0, 0, 1), Point(0, 5, 1), Point(0, 5, 0)), 0.0),
        ((Point(0, 0, 1), Point(1, 1, 1), Point(0, 1, 1), Point(0, 0, 0)), 45.00000000000001)
    ],
    'phone_number': [
        ('07895462130', '+7 (789) 546-21-30'),
        ('89875641230', '+7 (987) 564-12-30'),
        ('9195969878', '+7 (919) 596-98-78'),
        ('71234567890', '+7 (123) 456-78-90'),
        ('08889991122', '+7 (888) 999-11-22')
    ],
    'people_sort': [
        (('Mike Thompson 20 M', 'Robert Bustle 32 M', 'Andria Bustle 30 F'),
         ('Mr. Mike Thomson', 'Ms. Andria Bustle', 'Mr. Robert Bustle')),
        (('John Doe 0 M', 'Jill Smith -5 F', 'Bill McMill 100 G'),
         ('Ms. Jill Doe', 'Mr. John Doe', 'Ms. Bill Doe')),
        ((), ())
    ],
    'complex_numbers': [
        ((Complex(2, 1), Complex(5, 6)), ('7.00+7.00i', '-3.00-5.00i',
                                          '4.00+17.00i', '0.26-0.11i', '2.24+0.00i', '7.81+0.00i')),
        ((Complex(10, 11), Complex(-0.5, 3)), ('9.50+14.00i', '10.50+8.00i',
                                               '-38.00+24.50i', '3.03-3.84i', '14.87+0.00i', '3.04+0.00i')),
        ((Complex(-5, -10), Complex(5, 10)), ('0.00+0.00i', '-10.00-20.00i',
                                              '75.00-100.00i', '-1.00+0.00i', '11.18+0.00i', '11.18+0.00i'))
    ],
    'circle_square_mk': [
        ((10, 100), 314.159265),
        ((50, 50000), 7853.98163),
        ((1, 50), 3.14159265)
    ]
}


@pytest.mark.parametrize("input_data, expected", test_data['fact_it'])
def test_fact_it(input_data, expected):
    assert fact_it(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['fact_rec'])
def test_fact_rec(input_data, expected):
    assert fact_rec(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['show_employee'])
def test_show_employee(input_data, expected):
    assert show_employee(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['sum_and_sub'])
def test_sum_and_sub(input_data, expected):
    assert sum_and_sub(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['process_list'])
def test_process_list(input_data, expected):
    assert process_list(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['process_list_gen'])
def test_process_list_gen(input_data, expected):
    assert list(process_list_gen(input_data)) == expected


@pytest.mark.parametrize("input_data, expected", test_data['my_sum'])
def test_my_sum(input_data, expected):
    assert my_sum(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['my_sum_argv'])
def test_my_sum_argv(input_data, expected):
    assert run_script('my_sum_argv.py', input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['files_sort'])
def test_files_sort(input_data, expected):
    assert run_script('files_sort.py', (input_data,)) == expected


@pytest.mark.parametrize("input_data, expected", test_data['file_search'])
def test_file_search(input_data, expected):
    assert run_script('file_search.py', (input_data,)) == expected


@pytest.mark.parametrize("input_data, expected", test_data['email_validation'])
def test_email_validation(input_data, expected):
    assert fun(input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['fibonacci'])
def test_fibonacci(input_data, expected):
    assert list(map(cube, fibonacci(input_data))) == expected


@pytest.mark.parametrize("input_data, expected", test_data['average_scores'])
def test_average_scores(input_data, expected):
    assert list(map(lambda x: int(x * 10) / 10, compute_average_scores(input_data))) == expected


@pytest.mark.parametrize("input_data, expected", test_data['plane_angle'])
def test_plane_angle(input_data, expected):
    assert plane_angle(*input_data) == expected


@pytest.mark.parametrize("input_data, expected", test_data['phone_number'])
def test_phone_number(input_data, expected):
    assert wrapper(lambda x: x)((input_data,))[0] == expected


@pytest.mark.parametrize("input_data, expected", test_data['circle_square_mk'])
def test_circle_square_mk(input_data, expected):
    assert abs(circle_square_mk(*input_data) - expected) < 32
