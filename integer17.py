try:
    number = int(input("Введите целое число больше 999:"))
    hundreds = (number // 100)% 10
    print("Цифра сотен =", hundreds)
except ValueError:
    print('Ошибка! Введено не число.')
