'''Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.'''

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
a = int(input('Укажите количество чисел в списке: '))
numbrs = []
for i in range(a):
    numbrs.append(randint(1,10))
print(numbrs)

# БЫЛО
# b = 0
# count = 0
# numbrs2 = []
# if a % 2:
#     b = (a//2) + 1
# else:
#     b = (a//2)
# for j in range(b):
#     count = numbrs[j] * numbrs[a-1]
#     numbrs2.append(count)
#     a = a - 1
# print(numbrs2)

# СТАЛО
def multiply(lst: list):
    repeats = len(lst) // 2 if len(lst) % 2 == 0 else len(lst) // 2 + 1
    return [lst[i] * lst[len(lst) - (i + 1)] for i in range(repeats)]


print(multiply(numbrs))