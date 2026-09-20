try:
    A = float(input("Введите число A: ")) 
    K = 0
    sum = 0.0
    while sum + 1 / (K + 1) < A:
        K += 1
        sum += 1 / K
    print("Наибольшее K:", K)
    print("Полученная сумма:",sum)
except:
    print("Ошибка! Неверные исходные данные")
