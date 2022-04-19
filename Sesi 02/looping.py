# While Loops
print("-- While Loops --")
n = 5
while n > 0:
    n -= 1
    print(n)
print("")

i = 1
while i < 6:
  print(i)
  i += 1
print("")

# Break Statements
print("-- Break Statements --")
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')
print("")

# Continue Statements
print("-- Continue Statements --")
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')
print("")

# Else Clause
print("-- Else Clause --")
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')
print("")

n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')
print("")

# Nested While Loops
print("-- Nested While Loops --")

# Contoh 1
print("Contoh 1")
age = 22
gender = 'M'

if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')
print("")

# Contoh 2
print("Contoh 2")
a = ['foo', 'bar']

while len(a):
    print(a.pop(0))
    
b = ['baz', 'qux']
    
while len(b):
    print('>', b.pop(0))
print("")

# One-Line While Loops
print("-- One-Line While Loops --")
n = 5
while n > 0: n -= 1; print(n)
print("")



# Looping Statement
print("-- Looping Statement --")

# Contoh 1
print("Contoh 1")
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)
print("")

# Contoh 2
print("Contoh 2")
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)
for k in d:
    print(d[k])
for k in d.values():
    print(k)
for k, v in d.items(): 
    print(k, ":", v) 
print("")

# Break Statements
print("-- Break Statements --")
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)
print("")

# Continue Statements
print("-- Continue Statements --")
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)
print("")

# Else Clause
print("-- Else Clause --")
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execute
print("")

for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break
  print(i)
else:
  print('Done.') 







