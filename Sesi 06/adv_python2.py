# generator

# def my_generator():
#     print("Inside my generator")
#     yield 'a'
#     yield 'b'
#     yield 'c'

# print(my_generator())
# print(next(my_generator()))
# print(next(my_generator()))
# print(next(my_generator()))
# print(next(my_generator()))

# def my_generator():
#     print("Inside my generator")
#     yield 'a'
#     yield 'b'
#     yield 'c'

# print(my_generator())

# for x in my_generator():
#     print(x)

# def counter_generator(low,high):    # 2 || 5,10
#     while low <= high:              # 3 || 5 6 7 8 9 10 11 x stop
#         yield low                   # 4 || 5 6 7 8 9 10
#         low += 1                    # 5 || 6 7 8 9 10 11

# for i in counter_generator(5,10):   # 1
#     print(i, end = ' ')             # 5 || 6 || 7 || 8

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
  print(i, end=" ")