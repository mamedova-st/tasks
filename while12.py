try:
    N = int(input("Введите число N: "))
    K = 0
    sum = 0
    while sum + (K + 1) < N:
        K += 1
        sum += K
    print("Наибольшее K:", K)
    print("Полученная сумма:", sum)
except:
    print("Ошибка! Неверные исходные данные")
