"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
by Mwesigwa david Keneth
"""

def capitalize(s):
    return s.upper()

if __name__ == '__main__':
    s = input('Please type any  word of your choice \n')
    print(capitalize(s))
