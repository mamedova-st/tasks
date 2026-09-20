try:
    n = int(input("Введите число Фибоначчи N: "))
    f1 = 1
    f2 = 1
    k = 2
    while f2 < n:
        next_f = f1 + f2
        f1 = f2
        f2 = next_f
        k = k + 1
    print("Порядковый номер K:", k)
except:
    print("Ошибка ввода данных")