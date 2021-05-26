'''
5. Write a Python program to solve the Fibonacci sequence using recursion.
'''

def function(number):
    if(number == 1 or number == 2):
        return 1
    else:
        return function(number - 1) + function(number -2)

print(function(7))