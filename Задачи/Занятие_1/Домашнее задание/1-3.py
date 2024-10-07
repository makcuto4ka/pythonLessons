# Задание 1
print('Задание 1')

import math 
r=int(input('Введите R:'))
p=round(2*math.pi*r,2)
s= round(math.pi*r**2,2)
print('Длина окружности с радиусом',r,'см равна',p)
print('Площадь окружности с радиусом',r,'см равна',s)

# Задание 2
print('Задание 2')

x=10
y= 55
print(x,y)
x,y=y,x
print(x,y)

# Задание 3
print('Задание 3')

import math 
l=int(input('Введите длину маятника:'))
g=9.81
t=round(2*math.pi*(l/g)**0.5,2)
print('Период колебания маятника',t)