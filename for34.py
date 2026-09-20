try:
    N = int(input("Введите целое число N:"))
    if N<=1:
        print("Ошибка! Число N должно быть больше 1")
    else:
        A1 = 1
        A2 = 2
        print(A1)
        print(A2)
        for k in range(3, N +1):
            A_next = (A1+2*A2)/3
            print(A_next)
            A1 = A2
            A2 = A_next
except:
    print("Ошибка! Неверный ввод данных") 
