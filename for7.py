try:
    A = int(input("Введите число A:"))
    B = int(input("Введите число B:"))
    if A>=B:
        print("Ошибка! Число A должно быть меньше B")
    else:
        sum = 0
        for i in range(A, B + 1):
            sum += i
        print(f"Сумма чисел от {A} до {B} = {sum}")
except ValueError:
    print("Ошибка: неверные исходные данные")
