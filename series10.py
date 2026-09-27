try:
    N = int(input(f"Введите количество целых чисел:"))
    has_positive = False
    for i in range(N):
        number = int(input(f"Введите целое число:"))
        if number>0:
            has_positive = True
    print("Есть ли положительные числа в наборе?",has_positive)
except:
    print("Неверные исходные данные")