#1
print('\n#1')

import numpy as np
import os
from matplotlib import pyplot as plt

dir = os.getcwd()
x = np.linspace(-2, 2, 1000)

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True
def f(x,a,b):
    y= (x**b+a**b)/x**b
    y[y > 20]=np.nan
    y[y < -20]=np.nan
    return y
plt.plot(x, f(x,a=1,b=1), label='a=1,b=1', color='red')  
plt.plot(x, f(x,a=2,b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x,a=1,b=2), label='a=1,b=2', color='green') 
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('f(x)=(x^b+a^b)/x^b')
plt.legend()
plt.grid()
plt.show()
plt.savefig(dir + '/Занятие_9_1.svg')

#2
print('\n#2')

import numpy as np
import os
from matplotlib import pyplot as plt

dir = os.getcwd()
x = np.linspace(0, 5, 1000)

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True
def f(x,a,b):
    y= (x**b+a**b)/x**b
    y[y > 20]=np.nan
    y[y < -20]=np.nan
    return y
plt.plot(x, f(x,a=1,b=1), label='a=1,b=1', color='red')  
plt.plot(x, f(x,a=2,b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x,a=1,b=2), label='a=1,b=2', color='green') 
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('f(x)=(x^b+a^b)/x^b')
plt.legend()
plt.grid()

plt.axes([0.35, 0.60, 0.25, 0.25]) 
x = np.linspace(0, 0.5, 1000)
plt.grid()
plt.title('Для малых x')
plt.plot(x, f(x,a=1,b=1), label='a=1,b=1', color='red')  
plt.plot(x, f(x,a=2,b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x,a=1,b=2), label='a=1,b=2', color='green')  

plt.axes([0.70, 0.30, 0.25, 0.25]) 
x = np.linspace(10, 20, 1000)
plt.grid()
plt.title('Для больших x')
plt.plot(x, f(x,a=1,b=1), label='a=1,b=1', color='red')  
plt.plot(x, f(x,a=2,b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x,a=1,b=2), label='a=1,b=2', color='green')  

plt.show()
plt.savefig(dir + '/Занятие_9_2.svg')

#3
print('\n#3')

import numpy as np
import os
from matplotlib import pyplot as plt

dir = os.getcwd()
x = np.linspace(-5, 0, 1000)

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True
def f(x,a,b):
    y= (x**b+a**b)/x**b
    y[y > 20]=np.nan
    y[y < -20]=np.nan
    return y
plt.plot(x, f(x,a=1,b=1), label='a=1,b=1', color='red')  
plt.plot(x, f(x,a=2,b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x,a=1,b=2), label='a=1,b=2', color='green') 
plt.plot(x, [0]*len(x), label='x=0', color='black')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('f(x)=(x^b+a^b)/x^b')
plt.legend()
plt.grid()

plt.axes([0.21, 0.17, 0.50, 0.25]) 
def f(x,a,b):
    y= (x**b+a**b)/x**b
    y[y > 3]=np.nan
    y[y < -3]=np.nan
    return y
x = np.linspace(-5, 0, 1000)
plt.grid()
plt.plot(x, f(x,a=1,b=1), label='a=1,b=1', color='red')  
plt.plot(x, f(x,a=2,b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x,a=1,b=2), label='a=1,b=2', color='green')  
plt.plot(x, [0]*len(x), label='x=0', color='black')

plt.show()
plt.savefig(dir + '/Занятие_9_3.svg')

#4
print('\n#4')

import numpy as np
import os
from matplotlib import pyplot as plt

dir = os.getcwd()
x = np.linspace(-5, 0, 1000)

plt.rcParams["figure.figsize"] = [5, 5]
plt.rcParams["figure.autolayout"] = True

fig, axes = plt.subplots(1,3,figsize=(15, 4))
def f(x,a,b):
    y= (x**b+a**b)/x**b
    y[y > 20]=np.nan
    y[y < -20]=np.nan
    return y
plt.plot(x, f(x,a=1,b=1), label='a=1,b=1', color='red')  
plt.plot(x, f(x,a=2,b=1), label='a=2,b=1', color='blue')
plt.plot(x, f(x,a=1,b=2), label='a=1,b=2', color='green') 
plt.plot(x, [0]*len(x), label='x=0', color='black')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('f(x)=(x^b+a^b)/x^b')
plt.legend()
plt.grid()



plt.show()
plt.savefig(dir + '/Занятие_9_3.svg')
