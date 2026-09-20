try:
    n = int(input("Введите число N: "))
    f1 = 1
    f2 = 1
    while f2 <= n:
        next_f = f1 + f2
        f1 = f2
        f2 = next_f
    print("Первое число Фибоначчи больше N:", f2)
except:
    print("Ошибка ввода данных")
    