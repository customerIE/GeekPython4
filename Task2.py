# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
N = int(input('Введите натуральное число: '))
num = N
numbers = []
a = 2
while a * a <= N:
    if N % a == 0:
        numbers.append(a)
        N //= a
    else:
        a += 1
if N > 1:
    numbers.append(N)
print(f'Простые множители числа {num}: ', numbers)