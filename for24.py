try:
    X = float(input("Введите вещественное число X: "))
    N = int(input("Введите целое число N: "))
    if N <= 0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        sum = 1
        current_power = 1
        current_factorial = 1
        znak = -1
        for i in range(1, N + 1):
            current_power *= X * X
            current_factorial *= (2 * i - 1) * (2 * i)
            sum += znak * (current_power / current_factorial)
            znak = -znak
        print(f"Итоговая сумма равна = {sum}")
except ValueError:
    print("Ошибка! Неверные исходные данные")
