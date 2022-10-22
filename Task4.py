# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от -100 до 100)многочлена
# и записать в файл многочлен степени k.
# k - максимальная степень многочлена, следующий степень
# следующего на 1 меньше и так до ноля.
# Коэффициенты расставляет random, поэтому при коэффициенте 0
# просто пропускаем данную итерацию степени.
import random
k = int(input("Введите натуральную степень k: "))
def rnd():
    return random.randint(-101,101)
def write_f(str):
    with open('1.txt', 'w') as f:
        f.write(str)
def lst_koef(m):
    lst = [rnd() for i in range(m+1)]
    return lst
def create_str(lst):
    print(lst)
    str = ''
    if len(lst) < 1:
        str='x = 0'
    else:
        for i in range(len(lst)):
            if lst[i] < 0 and i == 0:
                str += ' - '
            if lst[i] != 0 and i != (len(lst)-1) and i != (len(lst)-2):
                str += f'{abs(lst[i])}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    if lst[i+1]>0: 
                        str += ' + '
                    else:
                        str += ' - '
            elif i == (len(lst)-2) and lst[i] != 0:
                str += f'{abs(lst[i])}x'
                if lst[i+1] != 0:
                    if lst[i+1]>0: 
                        str += ' + '
                    else:
                        str += ' - '
            elif i == len(lst) - 1 and lst[i] != 0:
                str += f'{abs(lst[i])} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                str += ' = 0'
    return str
factors = lst_koef(k)
print(factors)
write_f(create_str(factors))
