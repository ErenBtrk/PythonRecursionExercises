'''
11. Write a Python program to find  the greatest common divisor (gcd) of two integers.
'''

def function(num1,num2):
    if(num1 == num2):
        return num1
    elif(num1 > num2):
        return function(num1-num2,num2)
    else:
        return function(num1,num2-num1)


print(function(72,20))
print(function(12,14))
print(function(81,33))