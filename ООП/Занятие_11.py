# class Point2D():
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
        
# class Point3D(Point2D):
#     __slots__=('_z',)
    
#     def __init__(self, x, y):
#         super().__init__(x, y)
        
#     @property
#     def z(self):
#         return self._z

#     @z.setter
#     def z(self, value):
#         raise AttributeError("z запрещено")
        
# pt3 = Point3D(10, 20, 30)
# print("pt3.z =", pt3.z)

# try:
#     pt3.z = 40 
# except AttributeError as e:
#     print("Ошибка при изменении pt3.z:", e)


# try:
#     print(pt3.__dict__)
# except AttributeError as e:
#     print("Ошибка при обращении к pt3.__dict__:", e)

# print("pt3.__slots__:", pt3.__slots__)
# print("pt3.x =", pt3.x)



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