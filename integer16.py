try:
    number = int(input("Введите трехзначное число:"))
    a = number // 100
    b = (number//10)% 10
    c = number % 10
    new_number = a*100 + c*10 + b
    print("Полученное число =", new_number)
except ValueError:
    print('Ошибка! Введено не число.')
