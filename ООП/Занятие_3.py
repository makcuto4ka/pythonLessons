#  №1
class BankAccount:
    
    @classmethod
    def create_empty_account(cls, __account_number):
        return cls(__account_number, __balance=0)
    
    @staticmethod
    def __deposit(amount):
        if amount > 0 and isinstance(amount, (int, float)):
            return amount
        raise ValueError ('!@!@@!@!@!')
    
    @staticmethod
    
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance    
        
        if not self.__deposit(balance):
            raise 
            

acc = BankAccount.create_empty_account("123456789")  
acc.deposit(500)  
acc.withdraw(200)  
print(acc.get_balance())  # Вывод: 300


#  №2

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    @staticmethod
    def check_password_strength(password):
        return len(password) >= 6

    @classmethod
    def create_default_user(cls, username):
        default_password = "default"
        return cls(username, default_password)

    def get_username(self):
        return self.__username

    def set_password(self, new_password):
        if not User.check_password_strength(new_password):
            raise ValueError("Пароль слишком короткий")
        self.__password = new_password

user = User.create_default_user("Alice")
print(user.get_username())  # Вывод: Alice
user.set_password("12345")  # Ошибка: пароль слишком короткий
user.set_password("securePass")  # Пароль успешно изменён


# №3

class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        if not Book.check_year(year):
            raise ValueError("Год издания должен быть целым числом и не в будущем")
        self.__year = year

    @staticmethod
    def check_year(year):
        current_year = 2024
        return isinstance(year, int) and year <= current_year

    @classmethod
    def create_default_year(cls, title, author):
        default_year = 2024
        return cls(title, author, default_year)

    def get_info(self):
        return f"{self.__title}, автор: {self.__author}, год: {self.__year}"
    
book1 = Book("1984", "George Orwell", 1949)
print(book1.get_info())  # Вывод: "1984, автор: George Orwell, год: 1949"

book2 = Book.create_default_year("Brave New World", "Aldous Huxley")
print(book2.get_info())  # Вывод: "Brave New World, автор: Aldous Huxley, год: 2024"