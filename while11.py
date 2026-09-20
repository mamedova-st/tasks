try:
    N = int(input("Введите число N: "))
    K = 0
    sum = 0
    while sum < N:
        K += 1
        sum += K
    print("Наименьшее K:", K)
    print("Полученная сумма:", sum)
except:
    print("Ошибка! Неверные исходные данные")
