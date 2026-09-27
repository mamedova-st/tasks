try:
    N = int(input("Введите количество чисел:"))
    product = 1
    for i in range(N):
        number = float(input(f"Введите вещественное число:"))
        part = int(number)
        print(f"Целая часть:",part)
        product = product*part
    print("Произведение всех дробных частей:",product)
except:
    print("Неверные исходные данные")