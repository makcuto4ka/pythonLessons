import math
class Shape:
    def __init__(self):
        pass
    def area():
        raise NotImplementedError('формулы не известны')
    def perimeter():
        raise NotImplementedError('формулы не известны')
class Circle(Shape):
    def __init__(self, r):
        self.r=r

    def area(self):
        return(math.pi * self.r**2)
    
    def perimeter(self):
        return(math.pi * self.r*2)
    
    def __setattr__(self, key, value):
            print('сорделька1')
            if key not in ['r']:
                print('сорделька2')
                raise AttributeError(f"Local attributes are not allowed")
            if self.validate(key, value):
                print('сорделька3')
                super().__setattr__(key, value)
            else: 
                print('сорделька47') 
                raise ValueError('Число должно быть положительным')
            
    @classmethod
    def validate(self, key, arg):
        print('сорделька')
        return type(arg)==int and (arg>=0)
    

    
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w=w
        self.h=h

    def area(self):
        return(self.w*self.h)
    
    def perimeter(self):
        return(2*(self.w+self.h))
    
    def __setattr__(self, key, value):
            if key not in ['w','h']:
                raise AttributeError(f"Local attributes are not allowed")
            if self.validate(key, value):
                super().__setattr__(key, value)
            else:  
                raise ValueError('Число должно быть положительным')
            
    @classmethod
    def validate(self, arg):
        return type(arg)==int and (arg>=0)

circle = Circle(3)
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())


class Animal:
    def sound():
        return('звук животного')
class Dog(Animal):
    