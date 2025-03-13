import math
import matplotlib.pyplot as plt
import numpy as np

class Derivate:
    def __init__(self, instance):
        self.instance=None

    def __call__(self, instance,x, dx=0.00001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x-dx))/ 2*dx
    def __get__(self, instance, owner):
        self.instance=instance
        return self
class ExponentialFunction:
    derivative = Derivate()
    def __init__(self,a):
        self.__a=a
    def __call__(self,x, *args, **kwds):
        self.__exp=self.__a*math.exp(x)
        return (self.__exp)

exp_func = ExponentialFunction(a=2)
print(exp_func(0))          # 2.0
print(exp_func.derivative(0))  # 2.0 (производная 2e^x в x=0)

# Построение графиков
exp_func.plot()



























import math
import matplotlib.pyplot as plt
import numpy as np

class Derivative:
    def __call__(self, instance, x):
        h = 1e-5
        return (instance(x + h) - instance(x - h)) / (2 * h)
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return lambda x: self(instance, x)

class ExponentialFunction:
    derivative = Derivative()
    
    def __init__(self, a):
        self.a = a
    
    def __call__(self, x):
        return self.a * math.exp(x)
    
    def plot(self):
        x_vals = np.linspace(-2, 2, 100)
        f_vals = [self(x) for x in x_vals]
        df_vals = [self.derivative(x) for x in x_vals]
        
        plt.figure()
        plt.plot(x_vals, f_vals, label=f'$f(x) = {self.a}e^x$')
        plt.plot(x_vals, df_vals, label=f"$f'(x) = {self.a}e^x$", linestyle='--')
        plt.title('Function and its Derivative')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()

# Пример использования
if __name__ == "__main__":
    exp_func = ExponentialFunction(a=2)
    print(exp_func(0))           # 2.0
    print(exp_func.derivative(0)) # 2.0
    
    exp_func.plot()