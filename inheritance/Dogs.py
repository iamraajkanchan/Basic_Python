from .Animals import Animal

class Dog(Animal):

    def __init__(self, name):
        super().__init__()
        self.name = name
        # To change the attribute of the base class use self, don't use super()
        self.speak = "barks"
        print("Dogs class is initialized")

    def speakMethod(self):
        # Use super() only to invoke base class methods.
        super().speakMethod()
        return f"{self.name} {self.speak}"