try:
    A = float(input("Введите число A:"))
    B = float(input("Введите число B:"))
    if A<=B:
        print("Ошибка! Число A должно быть больше B")
    else:
        while A>=B:
            A -= B
        print("Длина незанятой части A =", A)
except:
    print("Ошибка: неверные исходные данные")
            