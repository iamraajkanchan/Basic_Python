from Animals import Animals
class Dogs(Animals):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        super.speak = "barks"
        print("Dogs class is initialized")
        
    def speak(self):
        super.speakMethod()
        return f"{self.name} {super.speak}"