try:
    N = int(input("Введите целое положительное число N:"))
    K = int(input("Введите целое положительное число K:"))
    if N<=0 or K<=0:
        print("Ошибка! Числа должны быть больше 0")
    else:
        sum = 0
        for i in range(1, N+1):
            sum += float(i)**K
        print("Сумма =", sum)
except:
    print("Ошибка! Неверный ввод данных")
    