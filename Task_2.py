# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

a = list (map (int ,input ('Введите несколько чисел: ') .split ()))
i = 0 
j = len(a)-1
while i <= j:
    s = a[i] * a[j]
    j = j-1
    i = i+1
    print (s)