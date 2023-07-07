'''
Задача 32: 
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
вводим диапазон,напр 5 и 15, если значения из списка попадают в дипазон, то вывести его индекс
т.о. в выводе будет список из индексов
'''
from random import randint
print(list_1 := [randint(-10,10) for _ in range(5)])
first_num = int(input('Enter first number: '))
last_num = int(input('Enter last number: '))
list_2 = [item for item in range(first_num,last_num+1)]
index = []

for i in range (len(list_1) or len(list_2)):
    if list_1[i] in list_2:
        index.append(i)
print(index)

print([i for i in range(len(list_1) or len(list_2)) if list_1[i] in list_2])
