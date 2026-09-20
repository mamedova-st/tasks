try:
    S = float(input("Введите площадь круга S:"))
    D = 2 * (S / 3.14) ** 0.5
    L = 3.14 * D
    print("Диаметр круга D =", D)
    print("Длина окружности L =", L)
except ValueError:
    print('Ошибка! Введено не число.')
