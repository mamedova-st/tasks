try:
    L = float (input("Введите длину окружности:"))
    R = L / (2 * 3.14)
    S = 3.14 * R ** 2
    print("Радиус окружности R =", R)
    print("Площадь круга S =", S)
except ValueError:
    print('Ошибка! Введено не число.')
