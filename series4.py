try:
    N = int(input("Введите количество чисел:"))
    sum = 0
    product =1
    for i in range(N):
        number = float(input(f"Введите число:"))
        sum = sum+number
        product = product*number
    print("Сумма:", sum)
    print("Произведение:", product)
except:
    print("Неверные исходные данные")