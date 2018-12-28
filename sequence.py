"""
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input andthen check whether they are divisible 
 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
 by mwesigwa David keneth
 """
print("Enter a sequence of comma separated 4 digit binary numbers")
container = []

while True:
    user_input = input("Press enter when done:\n")
    my_list = user_input.split(",")
    break

for num in my_list:
    if int(num,10) % 5 == 0:
        container.append(num)
    else:
        pass

print("these numbers are divisible by 5:", container)
