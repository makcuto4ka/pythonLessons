'''   На занятие '''
print('На занятие')

#1
print('\n#1')

lastName,name= input('Ваши фамилия, имя?').split()
age= input('Сколько вам лет?')
address= input('Где вы живете?')
print('Ваши фамилия, имя',lastName,name)
print('Ваш возраст',age)
print('Вы живете в',address)

#2
print('\n#2')

import math 
x=int(input('Введите x:'))
t=int(input('Введите t:'))
z= round((9*math.pi*t+10*math.cos(x))/(math.pow(t,0.5)- abs(math.sin(t)))*math.e**x,2)
print(z)


'''   Домашняя работа '''
print('\nДомашняя работа')

#1
print('\n#1')

import math 
r=int(input('Введите R:'))
p=round(2*math.pi*r,2)
s= round(math.pi*r**2,2)
print('Длина окружности с радиусом',r,'см равна',p)
print('Площадь окружности с радиусом',r,'см равна',s)

#2
print('\n#2')

x=10
y= 55
print(x,y)
x,y=y,x
print(x,y)


#3
print('\n#3')

import math 
l=int(input('Введите длину маятника:'))
g=9.81
t=round(2*math.pi*(l/g)**0.5,2)
print('Период колебания маятника',t)