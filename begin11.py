try:
    a = float(input("Введите первое число a:"))
    b = float(input("Введите второе число b:"))
    abs_a = abs(a)
    abs_b = abs(b)
    print("Сумма модулей =", abs_a + abs_b)
    print("Разность модулей =", abs_a - abs_b)
    print("Произведение модулей =", abs_a * abs_b)
    print("Частное модулей =", abs_a / abs_b )
except ValueError:
    print('Ошибка! Введено не число.')
