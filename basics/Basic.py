class Basic:    

    programmerName = "Raj Kanchan"

    def __init__(self):
        print("Basic class initialized.")

    '''
    # self is just a convention - you can name it anything you want, but everyone uses 'self'of.
    # It's automatically passed by Python when you call the method.
    # self represents the specific instance of the class, allowing access to its attributes and methods.
    # Without self, you cannot access instance variables or methods from within the class.

    '''

    def simpleMethod(self):
        print("This is a simple method in the Basic class.")

    def simpleMethodWithParameter (self, newName):

        print(f"Changing programmer name from {self.programmerName} to {newName}")
        self.programmerName = newName
        print(f"Programmer name changed to {self.programmerName}")