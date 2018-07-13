#Implement a Python function that is passed a list of numeric values and a particular threshold value,
#and returns the list with all values above the given threshold value set to 0. 
#The list should be altered as a side effect to the function call, and not by function return value. 

def returnList(thr, li1):
    for i in range(0,len(li1)):
        if li1[i] > thr:
            li1[i] = 0
            
threshold = int(input('Please write threshold value:    '))

num1 = int(input('Please write num1 to a list of numeric values:    '))
num2 = int(input('Please write num2 to a list of numeric values:    '))
num3 = int(input('Please write num3 to a list of numeric values:    '))

list1 = [num1, num2, num3]

returnList(threshold, list1 )
print(list1)