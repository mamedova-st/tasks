try:
    a = float(input("Введите длину ребра куба a:"))
    V = a ** 3
    S = 6 * a ** 2
    print("Объем куба =", V)
    print("Площадь поверхности =", S)
except ValueError:
    print('Ошибка! Введено не число.')
