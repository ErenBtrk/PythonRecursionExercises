'''
8. Write a Python program to calculate the harmonic sum of n-1.
Note: The harmonic sum is the sum of reciprocals of the positive integers.
Example :

'''

def function(n):
    if(n == 1):
        return 1
    else:
        return 1/n + function(n-1)

print(function(7))
print(function(4))
