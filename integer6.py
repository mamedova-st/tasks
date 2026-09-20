try:
    number = int(input("Введите двузначное число:"))
    left = number // 10
    right = number % 10
    print("Левая цифра (десятки) =", left)
    print("Правая цифра (единицы) =", right)
except ValueError:
    print('Ошибка! Введено не число.')
