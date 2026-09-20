try:
    price = float(input("Введите цену за 1 кг конфет:"))
    if price <=0:
        print("Ошибка! Цена должна быть больше 0")
    else:
        for i in range(1,11):
            kg = i / 10
            cost = price * kg
            print(f"{kg} кг ={cost} руб.")
except ValueError:
    print("Ошибка: неверные исходные данные")
