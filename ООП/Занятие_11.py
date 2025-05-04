class Point2D():
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
class Point3D(Point2D):
    __slots__=('_z',)
    
    def __init__(self, x, y):
        super().__init__(x, y)
        
    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        raise AttributeError("z запрещено")
        
pt3 = Point3D(10, 20, 30)
print("pt3.z =", pt3.z)

try:
    pt3.z = 40 
except AttributeError as e:
    print("Ошибка при изменении pt3.z:", e)


try:
    print(pt3.__dict__)
except AttributeError as e:
    print("Ошибка при обращении к pt3.__dict__:", e)

print("pt3.__slots__:", pt3.__slots__)
print("pt3.x =", pt3.x)



# 2
import timeit
import sys

class NormalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x += 1
        self.y += 1
        
class SlotPoint:
    __slots__ = ('x', 'y',)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x += 1
        self.y += 1

np=NormalPoint(1,1)

t1 = timeit.timeit(np.move, number=10000000)
print(t1)

sp=SlotPoint(1,1)
t1 = timeit.timeit(sp.move, number=10000000)
print(t1)



normal_size = sys.getsizeof(np) + sys.getsizeof(vars(np))
slot_size = sys.getsizeof(sp)

print(f"Размер NormalPoint: {normal_size} байт")
print(f"Размер SlotPoint: {slot_size} байт")



# 3


class Student():
    __slots__ = ('name', 'age', 'grade',)
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
class Student:
    __slots__ = ('name', 'age', 'grade')
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

def average_grade(students):
    total = sum(student.grade for student in students)
    return total / len(students)


students = [
    Student("Аня", 20, 85),
    Student("Миша", 21, 90),
    Student("Ваня", 22, 78),
    Student("Соня", 19, 92),
    Student("Саша", 20, 88)
]

avg = average_grade(students)


print(f"Средняя оценка студентов: {avg}")



# 4

class Product:
    __slots__ = ('name', 'price', 'quantity')
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def filter_products_by_price(products, threshold):
    return [product.name for product in products.values() if product.price > threshold]


products = {
    "Яблоки": Product("Яблоки", 80, 50),
    "Молоко": Product("Молоко", 120, 30),
    "Шоколад": Product("Шоколад", 150, 100),
    "Кофе": Product("Кофе", 300, 20),
    "Чай": Product("Чай", 200, 40)
}


print("Товары дороже 100 руб:", filter_products_by_price(products, 100))
print("Товары дороже 200 руб:", filter_products_by_price(products, 200))
print("Товары дороже 500 руб:", filter_products_by_price(products, 500))