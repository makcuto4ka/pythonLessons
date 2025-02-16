'''   На занятие '''
print('На занятие')

#1
print('\n#1')

try:
    a = int(input("Введите первое целое число \n"))
    b = int(input("Введите второе целое число \n"))
    c = int(input("Введите третье целое число \n"))
    if a<b:
        if a<c:
            y=a
        else:
            y=c
    else:
        if b<c:
            y=b
        else:
            y=c
    print("Минимальное число ", y)
except ValueError:
  print("Ошибка, вводи целые!")

#2
print('\n#2')

try:
    a = float(input("Введите первое число \n"))
    b = float(input("Введите второе число \n"))
    c = float(input("Введите третье число \n"))
    x1=1
    x2=3
    if a>=x1 and a<=x2:
        print("Число", a,'принадлежит отрезку',x1,x2)
    if b>=x1 and b<=x2:
        print("Число", b,'принадлежит отрезку',x1,x2)
    if c>=x1 and c<=x2:
        print("Число", c,'принадлежит отрезку',x1,x2)
except ValueError:
  print("Ошибка ввода!")



'''   Домашняя работа '''
print('\nДомашняя работа')

#1
print('\n#1')

a = float(input("Введите первое число \n"))
b = float(input("Введите второе число \n"))
try:
  print(a/b)
except ZeroDivisionError:
  print("Деление на 0!")

#2
print('\n#2')

s = float(input("Введите сумму покупки \n"))
if s>20:
    fs=s*0.65
else:
    fs=s
print('Итоговая сумма покупки',round(fs,2))
print('Размер предоставленной скидки',round(s-fs,2))


#3
print('\n#3')

m=int(input('Введите номер месяца: '))
month=['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
if 1<=m<=12:
    print('Месяц -',month[m-1],'Время года - ', end='')
    if m==12 or 1<=m<=2:
        print('Зима')
    elif 3<=m<=5:
        print('Весна')
    elif 3<=m<=5:
        print('Лето')
    else:
        print('Осень') 
else:
    print('Недопустимое число!')