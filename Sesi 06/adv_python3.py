# intro to decorator

# def say_hello(name):            # 4
#     return f"Hello {name}"      # Hello Bob

# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"

# def greet_bob(greeter_func):    # 2
#     return greeter_func("Bob")  # 3 

# print(greet_bob(say_hello))     #1


# def say_hello(name):            
#     return f"Hello {name}"      

# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"

# def greet_bob(greeter_func):    # 2
#     return greeter_func("Bob")  # be_awesome ("Bob")

# print(greet_bob(be_awesome))    # 1


# # Inner Functions
# def parent():
#     print("Printing from the parent() function")    # 1

#     def first_child():  # 6
#         print("Printing from the first_child() function")

#     def second_child(): # 3
#         print("Printing from the second_child() function")

#     second_child()      # 2
#     first_child()       # 5


# # Returning Functions From Functions
# def parent(num):                    # 2
#     def first_child():              # 7
#         return "Hi, I am Emma"      # 8

#     def second_child():
#         return "Call me Liam"

#     if num == 1:                    # 3
#         return first_child          # 4
#     else:
#         return second_child

# first = parent(1)                   # 1
# print(first)                        # 5
# print(first())                      # 6


# def parent(num):                    # 2
#     def first_child():
#         return "Hi, I am Emma"

#     def second_child():             # 6
#         return "Call me Liam"

#     if num == 1:                    # 3
#         return first_child          # 4
#     else:
#         return second_child

# first = parent(2)                   # 1
# print(first)
# print(first())

# # Simple Decorators
# def my_decorator(func):             # 2 func = say_whee
#     def wrapper():                  # 6 karena ini <function my_decorator.<locals>.wrapper at 0x00000198B2C3A290>
#         print("Something is happening before the function is called.")
#         func()                      # 8 say_whee()
#         print("Something is happening after the function is called.")
#     return wrapper                  # 3

# def say_whee():
#     print("Whee!")

# say_wheeeezz = my_decorator(say_whee)   # 1
# print(say_wheeeezz)                     # 4 <function my_decorator.<locals>.wrapper at 0x00000198B2C3A290>

# say_wheeeezz()


# def my_decorator(func):     # 4
#     def wrapper():          # 6
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper          # 5

# @my_decorator               # 3
# def say_whee():             # 2
#     print("Whee!")          # 9

# # say_whee = my_decorator(say_whee) 
# print(say_whee)
# say_whee()                  # 1


# import functools

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator


import functools
import time

def timer(func):            # 2 func = waste_some_time(1)
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):     # 4
        start_time = time.perf_counter()    # 5 get current time ketika/sebelum menjalankan func
        value = func(*args, **kwargs)       # 6 value = waste_some_time(1)
        end_time = time.perf_counter()       # 10 get current time ketika /
        run_time = end_time - start_time    # 11 
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")     # 12
        print(f"from {start_time} to {end_time}")
        return value    # 13

    return wrapper_timer    # 3

@timer
def waste_some_time(num_times): # 2
    for _ in range(num_times):  # 7 for _ in range(1)
        sum([i**2 for i in range(10000)])
        # 8 setiap i dari 0 sd 1000 dihitung pangkat 2 nya berapa

    # 9 kalau num_times > 1
    # untuk setiap iterasisampai perulangannya berakhir itu lakukan : sum 


# waste_some_time(1)
waste_some_time(999) # Finished 'waste_some_time' in 3.2479 secs