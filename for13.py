try:
    N = int(input("Введите количество слагаемых N:"))
    if N <= 0:
        print("Ошибка! Число N должно быть больше 0.")
    else:
        sum = 0
        znak = 1
        for i in range(1, N + 1):
            chislo = 1 + (i / 10)
            sum += znak * chislo
            znak = -znak
        print(f"Итоговый результат равен = {sum}")
except ValueError:
    print("Ошибка! Неверные исходные данные")
    