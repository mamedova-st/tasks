try:
    N = int(input("Введите целое число N:"))
    if N<=0:
        print("Ошибка! Число N  должно быть больше 0")
    else:
        sum = 0
        for i in range(N, 2*N + 1):
            sum += i**2
        print(f"Итоговая сумма = {sum}")
except ValueError:
    print("Ошибка: неверные исходные данные") 
    