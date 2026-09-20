try:
    R = float(input("Введите радиус круга R:"))
    L = 2 * 3.14 * R
    S = 3.14 * R ** 2
    print("Длина окружности L =", L)
    print("Площадь круга S =", S)
except ValueError:
    print('Ошибка! Введено не число.')
