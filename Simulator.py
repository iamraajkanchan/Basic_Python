# To run the program, use the command `python Simulator.py`
from encapsulation.BankUser import BankUser
from inheritance.Cats import Cat
from basics.Basic import Basic
from inheritance.Dogs import Dog
from abstraction.Car import Car
# basics is the name of the package and Basic.py is the name of file which contains the Basic class

basic = Basic()
basic.simple_method()
basic.simple_method_with_parameter("Abhishek Tiwari")
basic.simple_string_array()
basic.create_all_numeric_variables()
basic.create_all_character_variables()
basic.create_all_boolean_variables()
basic.create_all_sequence_variables()

truffles = Dog("Truffles")
print(truffles.speak_method())

ivy = Cat("Ivy")
print(ivy.eat_method())
print(ivy.speak_method())

chevrolet = Car("Chevrolet")
print(chevrolet.start())
print(chevrolet.stop())

raj = BankUser()
raj.set_user_name("Tony Stark")
raj.set_user_bank_name("HDFC Bank Limited")
raj.set_balance(43000.50)

print(raj.get_user_name())
print(raj.get_user_bank_name())
print(raj.get_balance())