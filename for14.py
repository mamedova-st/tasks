try:
    N = int(input("Введите целое число N:"))
    if N <= 0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        sum = 0
        for i in range(1, N + 1):
            odd_number = 2 * i - 1
            sum += odd_number
        print(f"Квадрат числа N = {sum}")
except ValueError:
    print("Ошибка! Введено не целое число.")
