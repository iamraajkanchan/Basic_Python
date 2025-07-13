from .Animals import Animal
class Dog(Animal):

    def __init__(self, name):
        super().__init__()
        self.name = name
        # To change the attribute of the base class use self, don't use super()
        self.speak = "barks"
        print("Initializing a derived Dog Object.")

    def speak_method(self):
        # Use super() only to invoke base class methods.
        super().speak_method()
        return f"{self.name} {self.speak}"