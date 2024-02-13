#Revmoe pass and complete the cat class
class Cat():
    def __init__(self):
        self.name = "unknown"
        self.age = 0
    def speak(self):
        print("Meow")


#Create objects here
#These should NOT be indented inside the class
import cat
garfield = cat.Cat()
garfield.name = "Garfield"
garfield.age = 50

stella = cat.Cat()
stella.name = "Stella"
stella.age = 7
 
#test didnt run lets try again