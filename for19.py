try:
    N = int(input("Введите целое число N: "))
    if N <= 0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        factorial = 1.0
        for i in range(1, N + 1):
            factorial *= i
        print(f"Факториал числа {N} равен: {factorial}")
except ValueError:
    print("Ошибка! Введено не целое число.")
    