try:
    A = int(input("Введите целое положительное число A:"))
    B = int(input("Введите целое положительное число B:"))
    if A>=B:
        print("Ошибка! Число A должно быть меньше B")
    else:
        for i in range(A, B+1):
            for c in range(i):
                print(i)
except:
    print("Ошибка! Неверный ввод данных")
    