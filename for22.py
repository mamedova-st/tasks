try:
    X = float(input("Введите вещественное число X: "))
    N = int(input("Введите целое число N: "))
    if N <= 0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        sum = 1
        current_power = 1
        current_factorial = 1
        for i in range(1, N + 1):
            current_power *= X
            current_factorial *= i
            sum += current_power / current_factorial
        print(f"Итоговая сумма равна = {sum}")
except ValueError:
    print("Ошибка! Неверные исходные данные")
