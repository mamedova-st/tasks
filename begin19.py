try:
    x1 = float(input("Введите x1:"))
    y1 = float(input("Введите y1:"))
    x2 = float(input("Введите x2:"))
    y2 = float(input("Введите y2:"))
    a = abs(x2 - x1)  #это ширина
    b = abs(y2 - y1) #это длина
    P = 2 * (a + b)
    S = a * b
    print("Периметр прямоугольника P:", P)
    print("Площадь прямоугольника S:", S)
except ValueError:
    print('Ошибка! Введено не число.')
