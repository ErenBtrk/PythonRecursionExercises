'''
4. Write a Python program to get the factorial of a non-negative integer.
'''

def function(number):
    if(number == 0):
        return 1
    else:
        return number * function(number-1)


print(function(5))