# Задание 1
print('Задание 1')
lastName,name= input('Ваши фамилия, имя?').split()
age= input('Сколько вам лет?')
address= input('Где вы живете?')
print('Ваши фамилия, имя',lastName,name)
print('Ваш возраст',age)
print('Вы живете в',address)

# Задание 2
print('Задание 2')

import math 
x=int(input('Введите x:'))
t=int(input('Введите t:'))
z= round((9*math.pi*t+10*math.cos(x))/(math.pow(t,0.5)- abs(math.sin(t)))*math.e**x,2)
print(z)