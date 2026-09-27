try:
    N = int(input("Введите количество целых чисел:"))
    count_even = 0
    for i in range(N):
        number = float(input(f"Введите целое число:"))
        if number % 2== 0:
            print(f"Четное число:",number)
            count_even = count_even+1
    print("Количество четных чисел:",count_even)
except:
    print("Неверные исходные данные")