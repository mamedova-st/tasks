try:
    sum = 0
    for i in range(10):
        number =float(input(f"Введи вещественное число:"))
        sum = sum+number
        sr = sum/10
    print("Среднее арифмитическое:", sr)    
except:
    print("Неверные исходные данные")