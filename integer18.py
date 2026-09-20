try:
    number = int(input("Введите целое число больше 999:"))
    thousands = (number // 1000)% 10
    print("Цифра тысяч =", thousands)
except ValueError:
    print('Ошибка! Введено не число.')
