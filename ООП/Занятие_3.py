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