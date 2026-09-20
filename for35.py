try:
    N = int(input("Введите целое число N:"))
    if N<=2:
        print("Ошибка! Число N должно быть больше 2")
    else:
        A1 = 1
        A2 = 2
        A3 = 3
        print(A1)
        print(A2)
        print(A3)
        for k in range(4, N +1):
            A_next = A3 + A2 - 2*A1
            print(A_next)
            A1 = A2
            A2 = A3
            A3 = A_next
except:
    print("Ошибка! Неверный ввод данных") 