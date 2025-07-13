class Animals:
    eat = "food"
    speak = "language"
    live = "house"

    def __init__(self):
        print("Animals Class is initialized")

    def eatMethod(self):
        print("All Animals Eat")

    def speakMethod(self):
        print("All Animals Speak")

    def liveMethod(self):
        print("All Animals have a habitat")

class Dogs(Animals):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.speak = "barks"
        print("Dogs class is initialized")

    def speakMethod(self):
        return f"{self.name} {self.speak}"