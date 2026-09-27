try:
    count = 0
    number = int(input("Введите целое число:"))
    while number !=0:
        count = count+1
        number = int(input("Введите целое число:"))
    print("Количество целых чисел:",count)
except:
    print("Неверные исходные данные")