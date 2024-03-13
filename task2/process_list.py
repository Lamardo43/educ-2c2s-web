def process_list(arr):
    return [i**2 if i % 2 == 0 else i**3 for i in arr]

def process_list_gen(arr):
    for i in arr:
        yield i**2 if i % 2 == 0 else i**3


# Тестирование и сравнение скорости работы функций
# arr = list(range(1, 100000000))
# Время выполнения с использованием list comprehension: 22.2608003616333 секунд
# Время выполнения с использованием функции-генератора: 28.91222643852234 секунд
