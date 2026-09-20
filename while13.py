try:
    A = float(input("Введите число A: "))
    K = 0
    sum = 0.0
    while sum <= A:
        K += 1
        sum += 1 / K
    print("Наименьшее K:", K)
    print("Полученная сумма:", sum)
except:
    print("Ошибка! Неверные исходные данные")
