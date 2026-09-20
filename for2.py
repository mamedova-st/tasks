try:
    A = int(input("Введите число A:"))
    B = int(input("Введите число B:"))
    if A>=B:
        print("Ошибка! Число A должно быть меньше B")
    else:
        for i in range(A, B +1):
            print(i)
        N = B - A + 1
        print(f"Количество этих чисел N = {N}")
except ValueError:
    print("Ошибка: неверные исходные данные")
