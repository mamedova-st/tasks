try:
    N =int(input("Введите целое число N:"))
    if N<=0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        A = 1
        for k in range(1, N +1):
            A =(A + 1) / k
            print(A)    
except:
    print("Ошибка! Неверный ввод данных")
    