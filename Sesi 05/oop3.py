# parent class
class Dog:
    # class attribute
    species = "Canis familiaris 2000"
    fav_meal = "Fav meal 2022"

    # def __init__(self, name, age, breed):
    #     self.name = name
    #     self.age = age
    #     self.breed = breed

    def __init__(self, name, age):
        # instance attribute
        self.name = name
        self.age = age
        
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
        # return self.name + 'is' + str(self.age) + 'years old'

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
        # return self.name + 'says' + sound
    
    def __repr__(self):
        return f"to create instance :: Dog (name={self.name}, age={self.age}, breed={self.breed}) #REPR"
    
    def __str__(self):
        return f"clean info :: {self.name} is {self.age} years old {self.breed} #STR"

# child class
class JackRussellTerrier(Dog):
    # kalau didefinisikannya seperti ini
    # JRT ini merupakan child class dari Dog class
    # parent class nya : Dog class
    # pass
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

# initiating new instance of JackRussellTerrier
# miles = Dog("Miles", 4, "JackRussellTerrier")
miles = JackRussellTerrier ("Miles", 4)

print('REPR and STR part')

print(repr(miles))
print(miles.__repr__())

print(str(miles))
print(miles.__str__())

# initiating new instance of Dachshund
# buddy = Dog("Buddy", 9, "Dachshund")
buddy = Dachshund ("Buddy", 9)

# initiating new instance of Bulldog
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")
jack = Bulldog ("Jack", 9)
print(jack.__dict__())
jim = Bulldog ("Jim", 5)
print(jim.__dict__())

# print(miles.name, miles.age, miles.breed)
# print(buddy.name, buddy.age, buddy.breed)
# print(jack.name, jack.age, jack.breed)
# print(jim.name, jim.age, jim.breed)

print(miles.name, miles.age)
print(buddy.name, buddy.age)
print(jack.name, jack.age)
print(jim.name, jim.age)

print(miles.speak())
print(buddy.speak("Yap"))
print(jim.speak("Woof"))
print(jack.speak("Woof"))

print(miles.description())
print(buddy.description())
print(jack.description())
print(jim.description())

print(miles.species)
print(buddy.species)
print(jack.species)
print(jim.species)

print(miles.fav_meal)
print(buddy.fav_meal)
print(jack.fav_meal)
print(jim.fav_meal)

# dog1 = Dog('miley',2)
# dog2 = Dog('abby', 2)
# # print(dog1.name, dog1.age, dog1.species)
# print(dog1.inst_name, dog1.inst_age, dog1.species)
