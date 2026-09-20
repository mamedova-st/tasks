import math
try:
    N = int(input("Введите целое число N: "))
    A = float(input("Введите начальную точку A (в радианах): "))
    B = float(input("Введите конечную точку B (в радианах): "))
    if N <= 0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        h = (B - A) / N
        print(f"Длина шага h равна: {h}")
        for i in range(N + 1):
            x = A + i * h
            f = 1 - math.sin(x)
            print(f"Значение функции в точке {x}: {f}")
except:
    print("Ошибка! Неверный ввод данных")
    