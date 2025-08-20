# Use PascalCase to define a class in Python, just like we do in Java.

class Basic:

    # Use snake case to define a variable and functions in Python, unlike camel case in Java.
    programmer_name = "Raj Kanchan"

    def __init__(self):
        print("Basic class initialized.")

    '''
    # self is just a convention - you can name it anything you want, but everyone uses 'self'of.
    # It's automatically passed by Python when you call the method.
    # self represents the specific instance of the class, allowing access to its attributes and methods.
    # Without self, you cannot access instance variables or methods from within the class.

    '''
    def simple_method(self):
        print("This is a simple method in the Basic class.")

    def simple_method_with_parameter (self, new_name):
        print(f"Changing programmer name from {self.programmer_name} to {new_name}")
        self.programmer_name = new_name
        print(f"Programmer name changed to {self.programmer_name}")
    def simple_method_with_return_value(self):
        return False

    def simple_string_array(self) :
        languages = ["Kotlin", "Swfit", "Java", "Python"]
        print(languages)

    def create_all_numeric_variables(self) :
        simple_integer_number = 29
        simple_decimal_number = 1029.24
        simple_complex_number = 2 + 3j
        # f is used to concatenate string with a variable. Use it when you are printing a output.
        print(f"Simple Integer Number : {simple_integer_number}")
        print(f"Simple Decimal Number : {simple_decimal_number}")
    
    def create_all_character_variables(self) :
        simple_string = "Hello World!"
        print(f"Simple String : {simple_string}")
        simple_character = 'A'
        print(f"Simple Character : {simple_character}")
        
    def create_all_boolean_variables(self) :
        simple_true_boolean = True
        simple_false_boolean = False
        print(f"Simple True Boolean : {simple_true_boolean}")
        print(f"Simple False Boolean : {simple_false_boolean}")
        
    def create_all_sequence_variables(self) :
        # This is a ordered, mutable list
        evens = [2,4,6,8]
        print(f"Simple Ordered, Mutable List : {evens}")
        # This is a immutable list
        odds = (1,3,5,7,9)
        print(f"Simple Immutable List : {odds}")
        # This is a range
        numbers = range(9)
        print(f"Simple Range Starting from 0 to 8 {numbers}")
        for i in numbers :
            print(f"Value in numbers {i}")
        # This is limited range
        new_numbers = range(10, 20)
        print(f"Simple Range Starting from 10 to 19 {new_numbers}")
        for i in new_numbers:
            print(f"Value in new_numbers {i}")

    def example_of_while_loop(self):
        numbers = [1,2,3,4,5]
        i = 0
        while i < len(numbers):
            print(f"Get array element using while loop: {numbers[i]}")
            i += 1

    def example_of_for_loop(self):
        numbers = [1,2,3,4,5]
        for i in numbers:
            print(f"Get array element using for loop: {i}")

    def example_of_basic_if_else_condition(self, i):
        if i % 2 == 0:
            print("The parameter of this function is an even number")
        else:
            print("The parameter of this function is an odd number")

    # Note to use the match condition you have to update the python to 3.10+
    def example_of_basic_match_condition(self, i):
        match i:
            case 1:
                return "Sunday"
            case 2:
                return "Monday"
            case 3:
                return "Tuesday"
            case 4:
                return "Wednesday"
            case 5:
                return "Thursday"
            case 6:
                return "Friday"
            case 7:
                return "Saturday"
        return None

