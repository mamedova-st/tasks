try:
    number = int(input("Введите трехзначное число:"))
    hundreds = number // 100
    print("Первая цифра (сотни):", hundreds)
except ValueError:
    print('Ошибка! Введено не число.')
