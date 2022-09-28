# Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами, выводится на экран, затем перемешивается, опять выводится на экран.

from random import randint
n = int(input("Введите количество элементов списка: "))
random_array = [randint(10, 99) for i in range(n)]
print(random_array)
for i in range(n):
    temp = random_array[i]
    j = randint(0, n-1)
    random_array[i] = random_array[j]
    random_array[j] = temp
print(random_array)