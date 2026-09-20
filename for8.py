try:
    A = int(input("Введите число A:"))
    B = int(input("Введите число B:"))
    if A>=B:
        print("Ошибка! Число A должно быть меньше B")
    else:
        prod = 1
        for i in range(A, B + 1):
            prod *= i
        print(f"Произведение чисел от {A} до {B} = {prod}")
except ValueError:
           print("Ошибка: неверные исходные данные")
           