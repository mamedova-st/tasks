try:
    a = int(input("Введите первое число A: "))
    b = int(input("Введите второе число B: "))
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    print("Наибольший общий делитель (НОД):", a)
except:
    print("Ошибка ввода данных")
    