class LoggedClass:
    def __getattribute__(self, name):
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Accessed attribute {name}\n")
        return super().__getattribute__(name)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


class Coordinates(LoggedClass):
    def __new__(cls, x, y):
        if x < 0 or y < 0:
            raise ValueError("x и y — неотрицательные числа")
        instance = super().__new__(cls)
        return instance

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    

c = Coordinates(3,4)  # OK, distance=5  
# c = Coordinates(-1,2)  # ValueError  
print(c.distance)  # 5.0  
obj = LoggedClass()  
