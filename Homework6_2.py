'''Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11 '''

# Было

# a = str(input('Введи любое вещественное число: '))
# sum = 0
# for i in range (len(a)):
#     if a[i].isdigit():
#         sum += int(a[i])
# print(sum)

# Стало

a = input('Введи любое вещественное число: ')
def summa(num: str):
    return sum([int(num[i]) for i in range(len(num)) if num[i].isdigit()])
print(summa(a))