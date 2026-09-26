try:
    sum = 0
    for i in range(10):
        number =float(input(f"Введи дробное число:"))
        sum = sum+number
    print("Сумма:",sum)
except:
    print("Неверные исходные данные")