try:
    n = int(input("Введите целое положительное число N: "))
    count = 0
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit
        count = count + 1
        n = n // 10
    print("Количество цифр:", count)
    print("Сумма цифр:", sum)
except:
    print("Ошибка ввода данных")
    