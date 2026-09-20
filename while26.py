try:
    n = int(input("Введите число Фибоначчи N: "))
    f1 = 1
    f2 = 1
    while f2 < n:
        next_f = f1 + f2
        f1 = f2
        f2 = next_f
    print("Предыдущее число Фибоначчи:", f1)
    print("Последующее число Фибоначчи:", f1 + f2)
except:
    print("Ошибка ввода данных")