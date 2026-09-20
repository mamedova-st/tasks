try:
    N = int(input("Введите число N: "))
    K = 1
    while K * K <= N:
        K += 1
    print("Наименьшее K:", K)
except:
    print("Ошибка! Неверные исходные данные")