# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

number = int(input("Введите количество элементов в массиве: "))
array = list()
for i in range(number):
    arr = int(input(f"Введите {i+1} элемент: "))
    array.append(arr)
    
print(array)

val = int (input("Введите любое число: "))
min_diff = abs(val - array[0])
min_val = array[0]
for el in array:
    if abs(val - el) < min_diff:
        min_diff = abs(val - el)
        min_val = el
print(f'Самый близкий к числу {val} => {min_val}')

