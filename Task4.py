# Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

try:
    n = int(input("Введите размерность пространства: "))
    list1 = [None for _ in range(n)]
    list2 = [None for _ in range(n)]
    for i in range(n):
        list1[i] = float(input(f"Введите {i+1} координату первой точки: "))
    for i in range(n):
        list2[i] = float(input(f"Введите {i+1} координату второй точки: "))
    sum = 0
    for i in range(n):
        sum = sum + (list1[i] - list2[i])**2
    print(f"Расстояние между точками = {sum**0.5}")
except:
    print("Необходимо вводить числа!")