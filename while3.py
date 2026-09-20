try:
    N = float(input("Введите целое число N:"))
    K = float(input("Введите целое число K:"))
    if N<=0 or K<=0:
        print("Ошибка! числа должны быть больше 0")
    else:
        a = 0
        while N>=K:
            N -=K
            a +=1
        print("Частное =", a)
        print("Остаток от деления =", N)
except:
    print("Ошибка: неверные исходные данные")
    