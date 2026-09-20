try:
    a = float(input("Введите сторону прямоугольника A: "))
    b = float(input("Введите сторону прямоугольника B: "))
    c = float(input("Введите сторону квадрата C: "))
    k1 = 0
    while a >= c:
        a = a - c
        k1 = k1 + 1
    k2 = 0
    while b >= c:
        b = b - c
        k2 = k2 + 1
    otvet = 0
    while k1 > 0:
        otvet = otvet + k2
        k1 = k1 - 1
    print("Максимальное количество квадратов:", otvet)
except:
    print("Ошибка ввода данных")