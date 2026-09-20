try:
    number = int(input("Введите трехзначное число:"))
    last = number % 10
    middle =(number // 10) % 10
    print("Последняя цифра(единицы) =", last)
    print("Средняя цифра(десятки) =", middle)
except ValueError:
    print('Ошибка! Введено не число.')
