# Задача 16: Требуется вычислить, 
# сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

number = int(input("Введите количество элементов в массиве: "))
array = list()
for i in range(number):
    arr = input(f"Введите {i+1} элемент: ")
    array.append(arr)
    
print(' '.join(array))

find_val = input("Введите искомое значение: ")
count = 0
for el in array:
    if el == find_val:
        count +=1
print(f"Элемент {find_val} встречается в массиве => {count}")

