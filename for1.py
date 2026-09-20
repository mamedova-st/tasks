try:
    K = int(input("Введите число K:"))
    N = int(input("Введите число N:"))
    if N <= 0:
        print("Ошибка! N  должно быть больше 0")
    else:
        for i in range(N):
            print(K)
except ValueError:
    print("Ошибка: неверные исходные данные ")
    