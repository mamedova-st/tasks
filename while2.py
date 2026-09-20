try:
    A = float(input("Введите число A:"))
    B = float(input("Введите число B:"))
    if A<=B:
        print("Ошибка! Число A должно быть больше B")
    else:
        count = 0
        while A>=B:
            A -= B
            count += 1
        print("Количество отрезков:", count)
except:
    print("Ошибка: неверные исходные данные")
    