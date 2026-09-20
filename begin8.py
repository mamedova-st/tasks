try:
    a = float(input("Введите число a:"))
    b = float(input("Введите число b:"))
    sr_arifm = (a + b)/2
    print("Среднее арифметическое =", sr_arifm)
except ValueError:
    print('Ошибка! Введено не число.')
