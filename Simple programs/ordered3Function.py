#Write a Python function named ordered3 that is passed three integers, 
#and returns true if the three integers are in order from smallest to largest, 
#otherwise it returns false. 


def ordered3(integer):
    if integer[0] < integer[2]:
        print('True') 
    else:
        print('False')  
    
###############################

integ = [8,0,11]

ordered3(integ)