#Write a Python function named zeroCheck that is given three integers, 
#and returns true if any of the integers is 0, otherwise it returns false. 

def zeroCheck(integ):
    if 0 in integ:
        print('True') 
    else:
        print('False')
        
###############################

integers = [0,10,3]

zeroCheck(integers)

