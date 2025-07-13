# To run the program, use the command `python Simulator.py`
from basics.Basic import Basic
from inheritance.Animals import Dogs
# basics is the name of the package and Basic.py is the name of file which contains the Basic class

basic = Basic()
basic.simple_method()
basic.simple_method_with_parameter("Abhishek Tiwari")
basic.simple_string_array()
basic.create_all_numeric_variables()
basic.create_all_character_variables()
basic.create_all_boolean_variables()
basic.create_all_sequence_variables()

buddy = Dogs("Truffles")
print(buddy.speakMethod())