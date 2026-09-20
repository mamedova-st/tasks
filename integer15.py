try:
    number = int(input("Введите трехзначное число:"))
    a = number // 100
    b = (number//10)% 10
    c = number % 10
    new_number = b*100 + a*10 + c
    print("Полученное число =", new_number)
except ValueError:
    print('Ошибка! Введено не число.')
