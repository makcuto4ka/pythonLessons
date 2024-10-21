'''   На занятие '''
print('На занятие')

#1
print('\n#1')

def f(a):
  a0=a[0]
  a[0]=a[-1]
  a[-1]=a0
  return a
m = int(input('Введите длину массива: '))
a=[input() for i in range(m)]
print('Исходный массив:', a)
print('Полученный массив:', f(a))

#2
print('\n#2')
def f(x,y):
  a=x
  b=y
  while x!=0 and y!=0:
    if x > y:
      x=x%y
    else:
      y=y%x
  return str(a//(x+y))+'/'+str(b//(x+y))
a,b = map(int,input('Введите a и b: ').split())
d,c = map(int,input('Введите d и c: ').split())
print(f(a,b)) 
print(f(d,c)) 

#3
print('\n#3')
def f(a,b,r,x,y):
  return (x-a)**2 + (y-b)**2 == r**2
a,b,r = map(int,input('Введите a,b и r: ').split())
xP,yP = map(int,input('Введите p1 и p2: ').split())
xF,yF = map(int,input('Введите f1 и f2: ').split())
xL,yL = map(int,input('Введите l1 и l2: ').split())
print(f(a,b,r,xP,yP))
print(f(a,b,r,xF,yF))
print(f(a,b,r,xL,yL))
#4
print('\n#4')

from random import randint
m1=[randint(-100, 100) for x in range(15)]
m2=[randint(-100, 100) for x in range(15)]
m3=[randint(-100, 100) for x in range(15)]
print('Массив:',m1,'Сумма элементов: ',sum(m1),'Среднеарифметическое: ',sum(m1)/len(m1))
print('Массив:',m2,'Сумма элементов: ',sum(m2),'Среднеарифметическое: ',sum(m2)/len(m2))
print('Массив:',m3,'Сумма элементов: ',sum(m3),'Среднеарифметическое: ',sum(m3)/len(m3))


#5
print('\n#5')

def f(a,b):
  return (a**2+b**2)**0.5
from random import randint
a1,b1 = randint(0, 10),randint(0, 10)
a2,b2 = randint(0, 10),randint(0, 10)
print('Катеты первого треугольника: ',a1,b1,'гипотенуза: ', f(a1,b1))
print('Катеты второго треугольника: ',a2,b2,'гипотенуза: ', f(a2,b2))
if f(a1,b1)>f(a2,b2):
  print('Гипотенуза первого треугольника больше гипотенузы второго')
elif f(a1,b1)<f(a2,b2):
  print('Гипотенуза второго треугольника больше гипотенузы первого')
else:
  print('Гипотенузы равны')
  
#6
print('\n#6')

k = int(input('Введите k: '))
m=[]
for i in range(1,k+1):
  sumi=0
  for j in str(i):
    sumi+=int(j)**len(str(i))
  if sumi==i:
      m.append(i)
print('Числа Армстронга:', m)


'''   Домашняя работа '''
print('\nДомашняя работа')

#1
print('\n#1')

import math 
def f(x,y):
  return math.degrees(math.atan(x/y))
x1,x2 = map(float,input('Введите x1 и x2: ').split())
y1,y2 = map(float,input('Введите y1 и y2: ').split())
z1,z2 = map(float,input('Введите z1 и z2: ').split())
print(f(x1,x2))
print(f(y1,y2))
print(f(z1,z2))


#2
print('\n#2')
def p(n):
  s=bin(n)[2:]
  s1=s[:(len(s))//2]
  s2=s[(len(s)-1)//2+1:]
  return s1[::-1]==s2
def f(n):
  v=n
  d=2
  if n==1:
    return False
  else:
    while d<=n//2:
      if n%d==0:
        v=0
      d+=1
    if v==0:
      return False
    else:
      return p(v)
n = int(input('Введите n: '))
m=[]
for i in range(0,n+1):
  if f(i)==True:
      m.append(i)
print(m)
