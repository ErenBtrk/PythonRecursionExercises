'''
6. Write a Python program to get the sum of digits a non-negative integer.
'''
def function(number):
    if(number <= 0):
        return 0
    else:
        return number % 10 + function(number // 10)

print(function(12345))
print(function(345))
print(function(45))
print(function(111))
