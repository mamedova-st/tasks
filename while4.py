try:
    N = int(input("Введите целое число N:"))
    if N<=0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        while N%3 ==0:
            N //=3
        if N == 1:
            print("True")
        else:
            print("False")
except:
    print("Ошибка: неверные исходные данные")
