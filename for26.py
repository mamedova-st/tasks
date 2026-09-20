try:
    X = float(input("Введите вещественное число X: "))
    N = int(input("Введите целое число N: "))
    if N <= 0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        sum = 0
        zn = 1
        for i in range(N + 1):
            sum += zn * (X ** (2 * i + 1)) / (2 * i + 1)
            zn = -zn
        print(f"Итоговая сумма равна: {sum}")
except:
    print("Ошибка! Неверный ввод данных")
