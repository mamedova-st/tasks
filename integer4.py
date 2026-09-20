try:
    A = int(input("Введите целое положительное число A:"))
    B = int(input("Введите целое положительное число B:"))
    count = A // B
    print("Количество отрезков B =", count)
except ValueError:
    print('Ошибка! Введено не число.')
