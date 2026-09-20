try:
    N = int(input("Введите целое число N:"))
    if N<=0:
        print("Ошибка! Число N должно быть больше 1")
    else:
        F1 = 1
        F2 = 1
        print(F1)
        print(F2)
        for k in range(3, N +1):
            F_next = F1 + F2
            print(F_next)
            F1 = F2
            F2 = F_next
except:
    print("Ошибка! Неверный ввод данных") 
