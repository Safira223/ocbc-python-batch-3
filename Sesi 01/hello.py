print("Hello World!")
print("")

#Integers
print("-- Integers --")
print(12243435678 +1)
print(type(12243435678 +1))
print(10)
print(type(10))
print("")


#Floating-Point Numbers
print("-- Floating-Point Numbers --")
print(4.2)
print(type(4.2))
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)
print("")


#Strings
print("-- Strings --")
print("Hacktiv8")
print(type("Hacktiv8"))
print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')
print("")

#Boolean
("-- Boolean --")
print(type(True))
print(type(False))

#When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(100 > 200) #False
print(100 == 200) #False
print(100 < 200) #True
print('A' == 'A') #True
print('a' == 'A') #False
print("")


#Variable
print("-- Variable --")
print("Contoh 1")
var = 23.5
print(var)
print(type(var))
print("")

print("Contoh 2")
var = "Now I'm a string"
print(var)
print(type(var))
print("")


print("Contoh 3")
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
print("")


#Variable Assignment
print("-- Variable Assignment --")
print("Contoh 1")
n = 300
print(n)
print("")

print("Contoh 2")
a = b = c = 300
print(a, b, c)
print("")


#Variable Names
print("-- Variable Names --")
name = "Hacktiv8"
Age = 54
has_laptops = True
print(name, Age, has_laptops)
print("")


#Operators and Expressions
print("-- Operators and Expressions --")
print("Contoh 1")
a = 10
b = 20
print(a + b)
print("")

print("Contoh 2")
a = 10
b = 20
print(a + b - 5)
print("")


#Arithmetic Operators
print("-- Arithmetic Operators --")
a = 4
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print("")

#Comparison Operators
print("-- Comparison Operators --")
a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
print("")

#String Manipulation
print("-- String Manipulation --")
s = 'foo fOO'
t = 'bar'
# + and * Operators
print(s + t )
print(s * 4)#Case Conversion
print(s.capitalize()) #capitalize
print(s.title()) #title
print(s.lower()) #lowercase
print(s.swapcase()) #uppercase
print(s.capitalize() + t.swapcase())
print("")


#Python Lists
print("-- Python Lists --")
a = ['foo', 'bar', 'baz', 'qux']
print(a)
print("")


#Modifying List Value
print("-- Modifying List Value --")
print("Contoh 1")
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2] = 10
a[-2] = 20
print(a)
print("")

print("Contoh 2")
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)
print("")


#Python Tuples
print("-- Python Tuples --")
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print(t[0])
print(t[-1])
print("")

#Packing and unpacking
print("-- Packing and unpacking --")
(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')
print(s1)
print(s3)
print(type(s3))
print("")


#Defining and Accessing Dictionary
print("-- Defining and Accessing Dictionary --")
MLB_team = {    
    'Colorado': 'Rockies',    
    'Boston': 'Red Sox',    
    'Minnesota': 'Twins',
}
print(MLB_team['Minnesota'])
#Adding an entry to an existing dictionary
MLB_team['Kansas City'] = 'Royals'
print(MLB_team)
print("")


#Building a Dictionary Incrementally
print("-- Building a Dictionary Incrementally --")
person = {}
person['fname'] = 'Hack'
person['lname'] = 8
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
print(person)
print(person['children'][1])
print("")


#Line Continuation
print("-- Line Continuation --")
person1_age = 42
person2_age = 16
person3_age = 71

someone_is_of_working_age = (
    (person1_age >= 18 and person1_age <= 65)
    or (person2_age >= 18 and person2_age <= 65)
    or (person3_age >= 18 and person3_age <= 65)
)

print(someone_is_of_working_age)












