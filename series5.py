try:
    N = int(input("Введите количество чисел:"))
    sym_drob = 0
    for i in range(N):
        number = float(input(f"Введите дробное число:"))
        drob_part = number - int(number)
        print(f"Дробная часть:", drob_part)
        sum_drob = number + drob_part
    print("Сумма всех целых частей:",sum_drob)
except:
    print("Неверные исходные данные")