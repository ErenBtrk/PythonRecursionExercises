'''
10. Write a Python program to calculate the value of 'a' to the power 'b'. Go to the editor
Test Data :
(power(3,4) -> 81

'''

def function(number,power):
    if(power == 1):
        return number
    else:
        return number * function(number,power-1)


print(function(3,4))
print(function(10,2))
print(function(1,7))
print(function(2,2))