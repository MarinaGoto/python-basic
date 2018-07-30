#Program that prompts the user for two integer values and 
#displays the result of the first number divided by the second, 
#with exactly two decimal places displayed. 


int1 = int(input('First integer:  '))

int2 = int(input('Second integer:  '))

result = int1/int2

print('Result after deviding the 1st number by the 2nd', format(result, '.2f'))
