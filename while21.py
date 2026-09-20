try:
    n = int(input("Введите целое положительное число N: "))
    has_odd = False
    while n > 0:
        if (n % 10) % 2 != 0:
            has_odd = True
        n = n // 10
    print("Есть ли нечетные цифры?:", has_odd)
except:
    print("Ошибка ввода данных")