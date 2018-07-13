#Write a Python function named printAsterisks that is passed a positive integer value n, 
#and prints out a line of n asterisks. If n is greater than 75, then only 75 asterisks should be displayed. 


def printAsterisks(a):
    if a > 75:
        print('*' * 75)
    else:
        print('*' * a)

asterisks = int(input('Please write a number of Asterisks:    '))
printAsterisks(asterisks)