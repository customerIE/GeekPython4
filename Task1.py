# Вычислить число Пи c заданной точностью d.
# Комментарий: Я сделал вычисление pi через ряд Нилаканта.
d=int(input('Введите количество знаков после запятой для числа pi: '))
pi = 3.00
num1 = 2
num2 = 3
num3 = 4
for i in range(3):
    pi += 4 / (num1 * num2 * num3)
    num1 += 2
    num2 += 2
    num3 += 2
    pi -= 4 / (num1 * num2 * num3)
    num1 += 2
    num2 += 2
    num3 += 2
temp=(pi-int(pi))*(10**d)
temp1=float(int(pi)+int(temp)/(10**d))
print(f'Число pi с точностью {d} = ', temp1)
