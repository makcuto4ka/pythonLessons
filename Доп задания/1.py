import math
import numpy as np
x= int(input('Число '))
r=math.ceil(x ** 0.5)
lenx=len(str(x))
m=np.array([[' '*(lenx-1)+'*']*r]*r)
n=1
flag=0
for i in range(x):
    for j in range(i,r-i):
        m[i][j]=' '*(lenx-len(str(n)))+str(n)
        n+=1
        if n>x:
            flag=1
            break
    if flag==1:
            break
    for j in range(i+1,r-i):
        m[j][r-i-1]=' '*(lenx-len(str(n)))+str(n)
        n+=1
        if n>x:
            flag=1
            break
    if flag==1:
            break
    for j in range(i+1,r-i):
        m[r-i-1][r-j-1]=' '*(lenx-len(str(n)))+str(n)
        n+=1
        if n>x:
            flag=1
            break
    if flag==1:
            break
    for j in range(i+1,r-i-1):
        m[r-j-1][i]=' '*(lenx-len(str(n)))+str(n)
        n+=1
        if n>x:
            flag=1
            break
    if flag==1:
            break
for i in range(r):
    print(m[i])
######
print('Поворот:')
m2=np.array([[' '*(lenx-1)+'*']*r]*r)
for i in range(r):
    for j in range(r):
        m2[j][r-i-1]=m[i][j]
for i in range(r):
    print(m2[i])
    