from .Animals import Animal

class Dog(Animal):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.speak = "barks"
        print("Dogs class is initialized")

    def speakMethod(self):
        return f"{self.name} {self.speak}"