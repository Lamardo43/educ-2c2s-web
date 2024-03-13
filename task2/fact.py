def fact_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n-1)

def fact_it(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Тестирование и сравнение скорости работы функций

# При n = 993
# Рекурсивная функция выполнена за 0.031400399981066585 секунд
# Итеративная функция выполнена за 0.025344100024085492 секунд