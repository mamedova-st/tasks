try:
    X = float(input("Введите вещественное число X: "))
    N = int(input("Введите целое число N: "))
    if N <= 0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        sum = 1
        v = 1
        niz = 1
        for i in range(1, N + 1):
            if i > 1:
                v *= (2 * i - 3)
            niz *= (2 * i)
            sum += ((-1) ** (i - 1)) * v * (X ** i) / niz
        print(f"Итоговая сумма равна: {sum}")
except:
    print("Ошибка! Неверный ввод данных")