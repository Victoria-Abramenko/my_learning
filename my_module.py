# my_str = "Это код из модуля my_module"
#
# def my_func(name):
#     print(f"Привет {name} - {my_str}")

# import math
#
# def factorial_func(number):
#     return math.factorial(number)

from math import factorial

def factorial_func(number):
    return factorial(number)

print(__name__)  # __main__  если запустить сам my_module, то __name__ приобретает значение __main__

# так можно написать условие, чтобы код запускался только при непосредственном запуске этого модуля
if __name__ == "__main__":
    for i in range(5):
        print(i, end=", ")  #0, 1, 2, 3, 4, # только при запуске этого модуля