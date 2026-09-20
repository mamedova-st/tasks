try:
    bytes_count = int(input("Введите размер файлa в байтах:"))
    kilobytes = bytes_count // 1024
    print("Количество полных килобайтов =", kilobytes)
except ValueError:
    print('Ошибка! Введено не число.')
