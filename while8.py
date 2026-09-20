try:
    N = int(input("Введите число N: "))
    K = 1
    while K * K <= N:
        K += 1
    print("Наибольшее K:", K - 1)
except:
    print("Ошибка! Неверные исходные данные")
    