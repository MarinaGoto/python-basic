#Write a Python function named getContinue that displays to the user “Do you want to continue (y/n): ”, 
#and continues to prompt the user until either uppercase or lowercase 'y' or 'n' is entered,
#returning (lowercase) 'y' or 'n' as the function value. 

def getContinue(choice):
    looping = True
    while looping:
        if choice in ('y','Y','N','n'):
            if choice in ('y','Y'):
                    return 'y'
            elif choice in ('n','N'):
                    return 'n'           
        else:
            print('Please enter y or Y or N or n!!')
            choice = input('Do you want to continue?   ')     

decision = input('Do you want to continue (y/n):   ')
getContinue(decision) 