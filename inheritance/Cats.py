from .Animals import Animal
class Cat(Animal) :
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.speak = "meow"
        print("Initializing a derived Cat Object.")

    def eat_method(self):
        super().eat_method()
        return f"{self.name} {self.eat}"

    def speak_method(self):
        super().speak_method()
        return f"{self.name} {self.speak}"