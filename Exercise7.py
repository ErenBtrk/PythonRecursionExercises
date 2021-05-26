'''
7. Write a Python program to calculate the sum of the positive
integers of n+(n-2)+(n-4)... (until n-x =< 0). 
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30

'''

def function(n):
    if(n <= 0):
        return 0
    else:
        return n + function(n-2)

print(function(6))
print(function(10))