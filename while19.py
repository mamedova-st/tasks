try:
    n = int(input("Введите целое положительное число N: "))
    num = 0
    while n > 0:
        digit = n % 10
        num = num * 10 + digit
        n = n // 10
    print("Перевернутое число:", num)
except:
    print("Ошибка ввода данных")
    