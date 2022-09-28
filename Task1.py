# Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

try:
    n = float(input("Введите число: "))
    sum = 0

    def sum_integer (x):
        global sum
        while x % 10 != 0:
            sum = sum + x % 10
            x = x // 10

    def sum_fractional (x):
        global sum
        while round (x % 1, 3) > 0.0001:
            sum = sum + ((x * 10) // 1)
            x = round (x * 10 % 1, 3)

    if n % 1 != 0:
        integer_part = n // 1
        fraction_part = n % 1
        sum_integer (integer_part)
        sum_fractional (fraction_part)
    else:
        sum_integer (n)
     
    print(f"Сумма цифр = {sum}")

except:
    print("Необходимо вводить число!")