# 1

class Student:
    _count = 0  

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls._count += 1
        return instance

    def __init__(self, full_name, student_id, average_grade, enrollment_year):
        self.full_name = full_name
        self.student_id = student_id
        self.average_grade = average_grade
        self.enrollment_year = enrollment_year

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        if not isinstance(value, str):
            raise TypeError("ФИО должно быть строкой")
        parts = value.split()
        if len(parts) != 3:
            raise ValueError("ФИО должно состоять из трёх частей")
        for part in parts:
            if not part.isalpha():
                raise ValueError("ФИО должно состоять из букв")
        self.__full_name = value

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        if len(str(value)) != 8 or not str(value).isdigit():
            raise ValueError("ID студента должно состоять из восьми чисел")
        self.__student_id = value

    @property
    def average_grade(self):
        return self.__average_grade

    @average_grade.setter
    def average_grade(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Средний балл должен быть числом")
        if not 0<value<100:
            raise ValueError("Средний балл должен быть числом от 0 до 100")
        self.__average_grade = value

    @property
    def enrollment_year(self):
        return self.__enrollment_year

    @enrollment_year.setter
    def enrollment_year(self, value):
        if not isinstance(value, int):
            raise TypeError("Год поступления должен быть числом")
        if not 2000<value<2025:
            raise ValueError("Год поступления должен быть от 2000 до 2025")
        self.__enrollment_year = value



    @classmethod
    def from_string(cls, data_str):
        parts = data_str.split(',')
        if len(parts) != 6:
            raise ValueError("Данные о студенте должны быть из шести частей")
        surname, name, patronymic, id, grade, year = (part.strip() for part in parts)
        full_name = f"{surname} {name} {patronymic}"
        try:
            grade = float(grade)
        except ValueError:
            raise ValueError("Средний балл должен быть числом")
        try:
            year = int(year)
        except ValueError:
            raise ValueError("Год поступления должен быть числом")
        return cls(full_name, id, grade, year)
    

student1 = Student("Иванов Иван Иванович", 12345678, 85, 2021)

data = "Петров,Петр,Петрович,87654321,90,2020"
student2 = Student.from_string(data)
print(Student._count)  




# 2

class Product:
    def __new__(cls, name, price, quantity):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError(" не должна быть пустой строкой.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("должно быть положительным числом.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("целое число, не меньше нуля.")


        instance = super().__new__(cls)
        return instance

    def __init__(self, name, price, quantity):
        self._name = name.strip()
        self._price = float(price)
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("должно быть положительным числом.")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("целое число, не меньше нуля.")
        self._quantity = value


    @classmethod
    def from_string(cls, product_str):
        parts = product_str.split(';')
        if len(parts) != 3:
            raise ValueError("Строка должна состоять из трёх частей")
        name = parts[0].strip()
        price = float(parts[1])
        quantity = int(parts[2])
        return cls(name, price, quantity)
