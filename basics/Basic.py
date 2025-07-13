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

    def simpleStringArray(self) :
        languages = ["Kotlin", "Swfit", "Java", "Python"]
        print(languages)

    def createAllNumericVariables(self) :
        simpleIntegerNumber = 29
        simpleDecimalNumber = 1029.24
        simpleComplexNumber = 2 + 3j
        # f is used to concatenate string with a variable. Use it when you are printing a output.
        print(f"Simple Integer Number : {simpleIntegerNumber}")
        print(f"Simple Decimal Number : {simpleDecimalNumber}")
    
    def createAllCharacterVariables(self) :
        simpleString = "Hello World!"
        print(f"Simple String : {simpleString}")
        simpleCharacter = 'A'
        print(f"Simple Character : {simpleCharacter}")
        
    def createAllBooleanVariables(self) :
        simpleTrueBoolean = True
        simpleFalseBoolean = False
        print(f"Simple True Boolean : {simpleTrueBoolean}")
        print(f"Simple False Boolean : {simpleFalseBoolean}")
        
    def createAllSequenceVariables(self) :
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
        newNumbers = range(10, 20)
        print(f"Simple Range Starting from 10 to 19 {newNumbers}")
        for i in newNumbers:
            print(f"Value in newNumbers {i}")
        