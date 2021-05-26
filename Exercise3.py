'''
3. Write a Python program of recursion list sum. Go to the editor
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21

'''

def function(list,start,end):
    if(start == end):
        return 0
    else:
        if(isinstance(list[start],int)):
            return list[start] + function(list,start+1,end)
        else:
            return sum(list[start]) + function(list,start+1,end)

list1 = [1, 2, [3,4], [5,6],[7,8,9]]

print(function(list1,0,len(list1)))

