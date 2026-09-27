try:
    N = int(input(f"Введите количество целых чисел:"))
    count_odd = 0
    for i in range(N):
        number = int(input(f"Введите целое число:"))
        if number % 2 !=0:
            print(f"Номер нечетного числа в списке: {i + 1}")
            count_odd = count_odd + 1
    print("Всего нечетных чисел:", count_odd)
except:
    print("Неверные исходные данные")