try:
    number = int(input("Введите трехзначное число:"))
    hundreds = number // 100
    middle = (number // 10)% 10
    last = number % 10
    sum_res = hundreds + middle + last
    prod_res = hundreds * middle * last
    print("Сумма цифр =", sum_res)
    print("Произведение цифр =", prod_res)
except ValueError:
    print('Ошибка! Введено не число.')
