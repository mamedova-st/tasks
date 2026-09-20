try:
    n = int(input("Введите число N для проверки на простоту: "))
    is_prime = True
    divider = 2
    while divider * divider <= n:
        if n % divider == 0:
            is_prime = False
        divider = divider + 1
    print("Является ли число простым?:", is_prime)
except:
    print("Ошибка ввода данных")
    