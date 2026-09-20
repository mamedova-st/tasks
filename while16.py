try:
    p = float(input("Введите процент увеличения пробега P: "))
    k = 1
    day_run = 10.0
    s = 10.0
    while s <= 200:
        day_run = day_run + day_run * (p / 100)
        s = s + day_run
        k = k + 1
    print("Количество дней K:", k)
    print("Суммарный пробег S:", s)
except:
    print("Ошибка ввода данных")