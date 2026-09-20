try:
    d = float(input("Введите диаметр окружности d:"))
    L = 3.14 * d
    print("Длина окружности =", L)
except ValueError:
    print('Ошибка! Введено не число.')
