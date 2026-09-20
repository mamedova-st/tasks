try:
    x1 = float(input("Введите x1:"))
    y1 = float(input("Введите y1:"))
    x2 = float(input("Введите x2:"))
    y2 = float(input("Введите y2:"))
    distance = abs((x2 - x1)**2 + (y2 - y1)**2)** 0.5
    print("Расстояние между двумя точками =", distance)
except ValueError:
    print('Ошибка! Введено не число.')
