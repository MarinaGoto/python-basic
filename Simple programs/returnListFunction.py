# Task P 7 p.204
# Implement a Python function that is passed a list of numeric values and a particular threshold value,
# and returns the list with all values above the given threshold value set to 0. 
# The list should be altered as a side effect to the function call, and not by function return value. 

# Input 2 data : a list of numeric values and particular threshold value
###   For example: [1,2,3,4,5]  
# threshold value 3
# Output a list of integers: the list is the same as the input list except the value
# which is larger than the threshold value should be replaces with 0 
###   For example: [1,2,3,0,0]
# Restriction: there is no return statement in the function
# but the list passed into the function should be modified anyway 



# Step 1: Ask for 2 input
# Step 2: Create a function with two parameters 
# Algorithm:
# Step 3:
# check for each integer in the list from index 0 to len(list)-1
#   if n is larger than the threhold value
#      then we should replace n with 0 at where n is located 


def returnList(thr, li1):
    
    for i in range(0,len(li1)):
        if li1[i] > thr:
            li1[i] = 0
            
threshold = int(input('Please write threshold value:    '))

list1 = [int(x) for x in input('Please write list of numeric values:    ').split()]

returnList(threshold, list1 )
print(list1)


# The same but with while loop      
#    i = 0
#   while i < len(list1):
#        if list1[i] > value:
#            list1[i] = 0 
#        i = i + 1
    
