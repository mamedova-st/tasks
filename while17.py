try:
    n = int(input("Введите целое положительное число N: "))
    while n > 0:
        digit = n % 10
        print("Цифра:", digit)
        n = n // 10
except:
    print("Ошибка ввода данных")