"""
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
"""
def square():
    print([num**2 for num in range(1,21)][0:5])

square()