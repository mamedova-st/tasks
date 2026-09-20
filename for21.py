try:
    N = int(input("Введите целое число N: "))
    if N <= 0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        sum = 1
        current_factorial = 1
        for i in range(1, N + 1):
            current_factorial *= i
            sum += 1 / current_factorial
        print(f"Итоговая сумма ряда равна = {sum}")
except ValueError:
    print("Ошибка! Введено не целое число")