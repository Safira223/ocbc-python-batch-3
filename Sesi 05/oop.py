def nama_fungsi (parameter):
        pass

class Dog:
    # pass

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    # def __init__(self, inputted_name, inputted_age):
    #     self.name (atribut class) = inputted_name (parameter)
    #     self.age = inputted_age

        # self.name = 'Miles'
        # self.age = 4

# instantiating
dog1 = Dog('miles',2)
dog2 = Dog('abby', 2)
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)
