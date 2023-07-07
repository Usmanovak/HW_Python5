'''
Задача 30:  
Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов 
нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d, 
где а1 - первое число строки, n - кол-во чисел, d - шаг.
'''
list_1 = []
first_element = int(input('First element: '))
step = int(input('Step: '))
count_nums = int(input('Count numbers: '))
number = 0
for i in range(1, count_nums + 1):
    number = first_element + (i - 1) * step
    list_1.append(number)
print(sorted(list_1))

# number = first_element + (count_nums - 1) * step
# print(sorted([number for i in range (1, count_nums+1)]))