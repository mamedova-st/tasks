try:
    M = int(input("Введите массу в килограммах M:"))
    tons = M // 1000
    print("Количество полных тонн =", tons)
except ValueError:
    print('Ошибка! Введено не число.')
