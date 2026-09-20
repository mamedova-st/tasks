try:
    a = float(input("Введите длину ребра a:"))
    b = float(input("Введите длину ребра b:"))
    c = float(input("Введите длину ребра c:"))
    V = a * b * c
    S = 2 * (a * b + b * c + a * c)
    print("Объем параллелепипеда V=", V)
    print("Площадь поверхности параллелепипеда S=", S)
except ValueError:
    print('Ошибка! Введено не число.')
