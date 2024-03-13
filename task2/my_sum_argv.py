import sys


def my_sum(*args):
    return sum(args)


if __name__ == "__main__":
    # Преобразование аргументов командной строки в числа и вычисление их суммы
    args = [float(arg) for arg in sys.argv[1:]]
    result = my_sum(*args)

    # Вывод результата на стандартный поток вывода
    print(result)
