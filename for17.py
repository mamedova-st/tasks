try:
    A = float(input("Введите вещественное число A: "))
    N = int(input("Введите целое число N: "))
    if N <= 0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        sum = 1
        current_power = 1
        for i in range(1, N + 1):
            current_power *= A
            sum += current_power
        print(f"Итоговая сумма = {sum}")
except ValueError:
    print("Ошибка! Неверные исходные данные")
