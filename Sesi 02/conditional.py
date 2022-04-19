# If Statement
print("-- If Statement --")
x = 0
y = 5

if x < y:                           #truthy
    print('yes 1')

if y < x:                           #falsy
    print('yes 2')

if x:                               #falsy
    print('yes 3')

if y:                               #truthy
    print('yes 4')

if 'aul' in 'grault':               #truthy
    print('yes 5')

if 'quux' in ['foo', 'bar', 'baz']: # falsy
    print('yes 6')
print("")


# Grouping Statements
print("-- Grouping Statements --")
print("Contoh 1")
weather = 'nice'
if weather == 'nice':
# nice nice? True
# not so nice == nice? False
    print('Mom the lawn')
    print('Weed the garden')
    print('some following statement ...')
print("")

print("Contoh 2")
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
    
print('After conditional')
print("")

print("Contoh 3")
# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x
print("")

# Else and Elif Clauses
print("-- Else and Elif Clauses --")

# Contoh 1
print("Contoh 1")
x = 20
if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
print("")

x = 120
if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
print("")

# Contoh 2
print("Contoh 2")
hargaBuku = 20000
hargaMajalah = 5000
uang = 200

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")
print("")

hargaBuku = 20000
hargaMajalah = 5000
uang = 6000

if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")
print("")

# Contoh 3
print("Contoh 3")
name = 'Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")
print("")

# Contoh 4
print("Contoh 4")
var = 14
if var:                           #true
    print("This won't either")
elif 'a' in 'bar':                #true
    print('foo')
elif 1/0:                         #false
    print("This won't happen")
print("")

# One-Line If Statements
print("--  One-Line If Statements --")

# Contoh 1
print("Contoh 1")
if 'f' in 'foo': print('1'); print('2'); print('3')
print("")

# Contoh 2
print("Contoh 2")
x = 2
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')
print("")

x = 3
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')
print("")

x = 3
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')
print("")

# Conditional Expressions
print("-- Conditional Expressions --")

# Contoh 1
print("Contoh 1")
raining = False
print("Let's go to the", 'beach' if not raining else 'library') 

raining = True
print("Let's go to the", 'beach' if not raining else 'library')
print("")

# Contoh 2
print("Contoh 2")
age = 12
s = 'teen' if age < 21 else 'adult'
print(s)
print("")

age = 21
if age < 21:
    s = 'teen'
else:
    s = 'adult'
print(s)
print("")

# Contoh 3
print("Contoh 3")
a = 'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'
print(a)
print("")

# Pass Statement
print("-- Pass Statement --")
if True:
    pass
print('foo')



