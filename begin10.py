try:
    a = float(input("Введите первое число a:"))
    b = float(input("Введите второе число b:"))
    a_squared = a ** 2
    b_squared = b ** 2
    print("Сумма квадратов =", a_squared + b_squared)
    print("Разность квадратов =", a_squared - b_squared)
    print("Произведение квадратов =", a_squared * b_squared)
    print("Частное квадратов =", a_squared/b_squared)
except ValueError:
    print('Ошибка! Введено не число.')
