# Задание 1
print('Задание 1')
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
  
# Задание 2
print('Задание 2')

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