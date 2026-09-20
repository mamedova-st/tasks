try:
    N = int(input("Введите целое число N: "))
    A = float(input("Введите координату точки A: "))
    B = float(input("Введите координату точки B: "))
    if N <= 0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        h = (B - A) / N
        print(f"Длина шага h равна: {h}")
        for i in range(N + 1):
            x = A + i * h
            print(f"Точка {i}: {x}")
except:
    print("Ошибка! Неверный ввод данных")
    