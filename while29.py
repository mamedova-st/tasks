try:
    eps = float(input("Введите точность epsilon: "))
    k = 3
    a3 = 1.0
    a1 = 2.0
    a2 = (a3 + 2.0 * a1) / 3.0
    while abs(a2 - a1) >= eps:
        a3 = a1
        a1 = a2
        a2 = (a3 + 2.0 * a1) / 3.0
        k = k + 1
    print("Номер шага K:", k)
    print("Элемент A K-1:", a1)
    print("Элемент A K:", a2)
except:
    print("Ошибка ввода данных")