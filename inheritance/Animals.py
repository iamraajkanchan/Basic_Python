class Animal:
    eat = "food"
    speak = "language"
    live = "house"

    def __init__(self):
        print("Animals Class is initialized")

    def eatMethod(self):
        print(f"This animal eats {self.eat}")

    def speakMethod(self):
        print(f"This animal sounds {self.speak}")

    def liveMethod(self):
        print(f"This animal lives in {self.speak}")