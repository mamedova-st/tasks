try:
    A = float(input("Введите вещественное число A: "))
    N = int(input("Введите целое число N: "))
    if N <= 0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        prod = 1
        for i in range(1, N + 1):
            prod *= A
            print(f"Число {A} в степени {i} равно: {prod}")
except ValueError:
    print("Ошибка! Неверные исходные данные")
    