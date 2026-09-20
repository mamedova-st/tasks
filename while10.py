try:
    N = int(input("Введите число N: "))
    K = 0
    while 3**K < N:
        K += 1
    print("Наибольшее K:", K - 1)
except:
    print("Ошибка! Неверные исходные данные")
    