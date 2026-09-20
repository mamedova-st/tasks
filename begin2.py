try:
    a = float(input("Введите сторону квадрата a:" ))
    S = a ** 2
    print("Площадь квадрата S=", S)
except ValueError:
    print('Ошибка! Введено не число.')
