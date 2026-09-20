try:
    number = int(input("Введите двузначное число:"))
    left = number // 10
    right = number % 10
    new_number = right * 10 + left
    print("Число послe перестановки цифр =", new_number)
except ValueError:
    print('Ошибка! Введено не число.')
