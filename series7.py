try:
    N = int(input("Введите количество чисел:"))
    sum_rounded = 0
    for i in range(N):
        number = float(input(f"Введите дробное число:"))
        rounded = round(number)
        print(f"Округленное число: {rounded}")
        sum_rounded = sum_rounded+rounded
    print("Сумма округленных значений:",sum_rounded)
except:
    print("Неверные исходные данные")