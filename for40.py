try:
    A = int(input("Введите целое число A:"))
    B = int(input("Введите целое число B:"))
    if A>=B:
        print("Ошибка! Число B должно быть больше A")
    else:
        count = 1
        for i in range(A, B +1):
            for c in range(count):
                print(i)
            count += 1
except:
    print("Ошибка! Неверный ввод данных")
