try:
    A = int(input("Введите целое число A:"))
    B = int(input("Введите целое число B:"))
    if A>=B:
        print("Ошибка! Число A должно быть меньше B")
    else:
        for i in range(B - 1, A, -1):
            print(i)
        N =B - A -1 
        print(f"Количество этих чтсел N = {N}")
except ValueError:
    print("Ошибка:неверные исходные данные")
    