# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

a = list (map (int ,input ('Введите несколько чисел: ') .split ()))
print (a)
sum = 0
count = 1
while count < len (a):
    sum = sum + a[count]
    count = count + 2
print ('Сумма элементов списка, находящихся на нечетной позиции = ', sum)