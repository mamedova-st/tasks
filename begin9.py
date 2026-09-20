try:
    a = float(input("Введите неотрицательное число a:"))
    b = float(input("Введите неотрицательное число b:"))
    sr_geom = (a * b) ** 0.5
    print("Среднее геометрическое =", sr_geom)
except ValueError:
    print('Ошибка! Введено не число.')
