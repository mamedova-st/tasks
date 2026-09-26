try:
    product = 1
    for i in range(10):
        number = float(input(f"Введи вещественное число:"))
        product = product*number
    print("Произведение:", product)
except:
    print("Неверные исходные данные")