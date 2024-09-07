import math 
l=int(input('Введите длину маятника:'))
g=9.81
t=round(2*math.pi*(l/g)**0.5,2)
print('Период колебания маятника',t)