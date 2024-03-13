import random

def circle_square_mk(r, n):
    in_circle = 0
    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if x**2 + y**2 <= r**2:
            in_circle += 1
    square = (in_circle / n) * (4 * r**2)
    return square

# Введите радиус окружности: 1000
# Введите количество экспериментов: 1000
# Площадь окружности, вычисленная методом Монте-Карло: 3116000.0
# Площадь окружности по формуле: 3141592.653589793
# Погрешность: 25592.653589793015
