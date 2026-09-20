try:
    n = int(input("Введите число N для проверки в ряду Фибоначчи: "))
    f1 = 1
    f2 = 1
    while f2 < n:
        next_f = f1 + f2
        f1 = f2
        f2 = next_f
    if f2 == n or n == 1:
        print("Это число Фибоначчи?:", True)
    else:
        print("Это число Фибоначчи?:", False)
except:
    print("Ошибка ввода данных")
    