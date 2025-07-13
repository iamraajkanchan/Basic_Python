class Animal:
    eat = "food"
    speak = "language"
    live = "house"

    def __init__(self):
        print("Initializing the Base Animal Object.")

    def eat_method(self):
        print(f"This animal eats {self.eat} to feed himself/herself")

    def speak_method(self):
        print(f"This animal {self.speak} to speak")

    def live_method(self):
        print(f"This animal lives in {self.speak} to shelter himself/herself.")