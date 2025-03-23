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
        if not isinstance(value, str):
            raise ValueError("Data must be a string")
        self._data = value


class Coordinates(LoggedClass):
    def __new__(cls, x, y):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise ValueError("x and y must be numbers")
        if x < 0 or y < 0:
            raise ValueError("Coordinates must be non-negative")
        instance = super().__new__(cls)
        return instance

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5