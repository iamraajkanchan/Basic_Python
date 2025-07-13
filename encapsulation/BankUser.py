class BankUser:
    def __init__(self):
        # Use double underscore `__` to define a private attribute of a class.
        self.__name = None
        self.__bank_name = None
        self.__balance = None

    def set_user_name(self, name):
        self.__name = name


    def set_user_bank_name(self, bank_name):
        self.__bank_name = bank_name

    def set_balance(self, balance):
        self.__balance = balance

    def get_user_name(self):
        return self.__name

    def get_user_bank_name(self):
        return self.__bank_name

    def get_balance(self):
        return self.__balance