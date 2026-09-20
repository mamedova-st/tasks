try:
    number = int(input("Введите двузначное число:"))
    left = number // 10
    right = number % 10
    sum_res = left + right
    prod_res = left * right
    print("Сумма цифр =", sum_res)
    print("Произведение цифр =", prod_res)
except ValueError:
    print('Ошибка! Введено не число.')
