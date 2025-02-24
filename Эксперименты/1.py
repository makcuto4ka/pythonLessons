class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(", ")
        return cls(name, int(age))

p = Person.from_string("Иван, 25")
print(p.name, p.age)  # Иван 25