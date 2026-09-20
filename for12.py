try:
    N = int(input("Введите целое число N:"))
    if N<=0:
        print("Ошибка! Число N  должно быть больше 0")
    else:
        prod = 1
        for i in range(1, N +1):
            chislo = 1 + (i / 10)
            prod *= chislo
        print(f"Итоговая сумма = {prod}")
except ValueError:
    print("Ошибка: неверные исходные данные")
