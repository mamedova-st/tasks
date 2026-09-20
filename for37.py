try:
    N = int(input("Введите целое число N:"))
    if N<=0:
        print("Ошибка! Число N должно быть больше 0")
    else:
        sum = 0
        for i in range(1, N+1):
            sum += float(i) ** i
        print("Сумма =", sum)
except:
    print("Ошибка! Неверный ввод данных")
    