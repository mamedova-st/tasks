try:
    number = int(input("Введите трехзначное число:"))
    c1 = number // 100
    c2 = (number // 10)% 10
    c3 = number % 10
    new_number = c3 * 100 + c2 * 10 + c1
    print("Перевернутое число =", new_number)
except ValueError:
    print('Ошибка! Введено не число.')
