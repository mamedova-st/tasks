try:
    X = float(input("Введите вещественное число X: "))
    N = int(input("Введите целое число N: "))
    if N <= 0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        sum = X
        v = 1
        niz = 1
        for i in range(1, N + 1):
            v *= (2 * i - 1)
            niz *= (2 * i)
            sum += v * (X ** (2 * i + 1)) / (niz * (2 * i + 1))
        print(f"Итоговая сумма равна: {sum}")
except:
    print("Ошибка! Неверный ввод данных")