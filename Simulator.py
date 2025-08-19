# To run the program, use the command `python Simulator.py`
from utility.Util import Util
from enums.FuelType import FuelType
from abstraction.ElectricCar import ElectricCar
from abstraction.Motorcycle import MotorCycle
from abstraction.Car import Car
from encapsulation.BankUser import BankUser
from inheritance.Cats import Cat
from basics.Basic import Basic
from inheritance.Dogs import Dog
from abstraction.IndianCar import IndianCar
from abstraction.Jeep import Jeep
# basics is the name of the package and Basic.py is the name of file which contains the Basic class

basic = Basic()
Util.print_separation("Basic")
basic.simple_method()
basic.simple_method_with_parameter("Abhishek Tiwari")
print(f"{basic.simple_method_with_return_value()}")
basic.simple_string_array()
basic.create_all_numeric_variables()
basic.create_all_character_variables()
basic.create_all_boolean_variables()
basic.create_all_sequence_variables()

Util.print_separation("Inheritance")
truffles = Dog("Truffles")
print(truffles.speak_method())

ivy = Cat("Ivy")
print(ivy.eat_method())
print(ivy.speak_method())

Util.print_separation("Polymorphism")
print("Example Regarding Polymorphism")
# Polymorphism in Python
animals = [truffles, ivy]
for animal in animals:
    print(animal.speak_method())

print("-" * 100)

chevrolet = IndianCar("Chevrolet")
print(chevrolet.start())
print(chevrolet.stop())

raj = BankUser()
raj.set_user_name("Tony Stark")
raj.set_user_bank_name("HDFC Bank Limited")
raj.set_balance(43000.50)

print(raj.get_user_name())
print(raj.get_user_bank_name())
print(raj.get_balance())


#Function that can work with any Vehicle Implementation
def operate_vehicle(vehicle_object) :
    print(f"Operating a vehicle that uses {vehicle_object.get_fuel_type()}")
    print(vehicle_object.start_engine())
    print(vehicle_object.honk())
    print(vehicle_object.stop_engine())
    print("-" * 40)


normalCar = Car("Toyota", "Camry")
electricCar = ElectricCar("Tesla", "Model 3", 98)
motorcycle = MotorCycle("Hero", "Splendor +")

vehicles = [normalCar, electricCar, motorcycle]

for vehicle in vehicles:
    operate_vehicle(vehicle)

Util.print_separation( "Enum Example")

# Printing Enum Values
print(FuelType.ELECTRIC)
print(FuelType.ELECTRIC.value)

Util.print_separation("Abstraction Example")

myJeep = Jeep()
myJeep.start_engine()

Util.print_separation("While Loop Example")
basic.example_of_while_loop()

Util.print_separation("For Loop Example")
basic.example_of_for_loop()

Util.print_separation("Basic If Else Condition Example")
basic.example_of_basic_if_else_condition(3)

Util.print_separation("Basic If Else Condition Example")
basic.example_of_basic_if_else_condition(2)
