'''
9. Write a Python program to calculate the geometric sum of n-1. 
Note: In mathematics, a geometric series is a series with a constant ratio between successive terms.

'''

def function(n):
    if(n == 0):
        return 1
    else:
        return 1/2**n + function(n-1)

print(function(7))
print(function(4))