try:
    a = float(input("Введите катет a:"))
    b = float(input("Введите катет b:"))
    c = (a ** 2 + b ** 2) ** 0.5
    P = a + b + c
    print("Гипотенуза с =", c)
    print("Периметр P =", P)
except ValueError:
    print('Ошибка! Введено не число.')
