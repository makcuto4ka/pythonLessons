import math 
x=int(input('Введите x:'))
t=int(input('Введите t:'))
z= round((9*math.pi*t+10*math.cos(x))/(math.pow(t,0.5)- abs(math.sin(t)))*math.e**x,2)
print(z)