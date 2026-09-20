try:
    N = int(input("Введите целое число N:"))
    if N<=0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        factorial = 1.0
        while N>0:
            factorial *= N
            N -= 2
        print("Двойной факториал:", factorial)
except:
    print("Ошибка: неверные исходные данные")
