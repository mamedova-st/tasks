try:
    L = int(input("Введите расстояние в сантиметрах L:"))
    meters = L // 100
    print("Количество полных метров =", meters)
except ValueError:
    print('Ошибка! Введено не число.')
