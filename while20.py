try:
    n = int(input("Введите целое положительное число N: "))
    has_two = False
    while n > 0:
        if n % 10 == 2:
            has_two = True
        n = n // 10
    print("Есть ли цифра 2?:", has_two)
except:
    print("Ошибка ввода данных")