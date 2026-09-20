try:
    A = float(input("Введите координату точки A:"))
    B = float(input("Введите координату точки B:"))
    C = float(input("Введите координату точки C:"))
    length_AC = abs(A - C)
    length_BC = abs(B - C)
    sum = length_AC + length_BC
    print("Длина отрезка AC =", length_AC)
    print("Длина отрезка BC =", length_BC)
    print("Сумма отрезков AC и BC =", sum)
except ValueError:
    print('Ошибка! Введено не число.')
