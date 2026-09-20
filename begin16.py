try:
    x1 = float(input("Введите координату первой точки x1:"))
    x2 = float(input("Введите координату второй точки x2:"))
    distance = abs(x2 - x1)
    print("Расстояние между точками =", distance)
except ValueError:
    print('Ошибка! Введено не число.')
