# def dog_speak(self, sound):
#     pass

# def cat_speak(self, sound):
#     pass

# def dog_description(self):
#     pass

# def cat_description(self):
#     pass

# class Dog:

#     #class atribut
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#     #     # instance attribute
#         self.name = name 
#         self.age = age
    
    # def __init__(self):
    #     pass

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
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
    
# instantiating a new dog class
dog1 = Dog('miley',2)
dog2 = Dog('abby', 2)
# print(dog1.name, dog1.age, dog1.species)
# print(dog2.name, dog2.age, dog2.species)

buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

# print(buddy.name)
# print(miles.name)

# print(buddy.age)
# print(miles.age)

# print(buddy.species)
# print(miles.species)

# dog3 = Dog('', '')
# dog3 = Dog()
# print(dog3.species)

# description_of_buddy = buddy.description()
# print(description_of_buddy)
# or
print(buddy.description())
print(miles.description())
print(dog1.description())
print(dog2.description())

# sound_of_buddy = buddy.speak('Woof Woof')
# print(sound_of_buddy)
# sound_of_miles = buddy.speak('Bow Wow')
# print(sound_of_buddy)



