# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

try:
    n = int(input("Введите число: "))
    list = [1 for _ in range(n)]
    list[1] = 1
    for i in range(2, n + 1):
        list[i -1] = list[i - 2] * i
    print(list)
except:
    print("Необходимо вводить число!")