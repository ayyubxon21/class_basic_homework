#Create a "Person" class
#Create an attribute "name" in the "Person" class
class Person:
    def __init__(self,name):
        self.name = name
    def ism(self):
        return f"ism{self.name}"
x = Person(name = 'Ayyubxon')
print(x.ism())
