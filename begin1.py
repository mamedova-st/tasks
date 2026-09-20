try:
    a = float(input("Введите сторону квадрата a: "))
    P = 4 * a
    print("Периметр квадрата P =", P)
except ValueError:
    print('Ошибка! Введено не число.')
