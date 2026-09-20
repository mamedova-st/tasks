try:
    N = int(input("Введите целое число N:"))
    if N<=0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        A = 2
        for k in range(1, N+1):
            A = 2+ 1/A
            print(f"A{k} = {A}")
except:
    print("Ошибка! Неверный ввод данных")
                