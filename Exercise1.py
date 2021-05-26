'''
1. Write a Python program to calculate the sum of a list of numbers. 

'''

def function(list,start,end):
    if(start == end):
        return 0
    else:
        return list[start] + function(list,start+1,end)


list1 = [1,2,3,4,5,5]

print(function(list1,0,len(list1)))