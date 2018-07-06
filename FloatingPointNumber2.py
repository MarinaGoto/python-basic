#Write a Python program that prompts the user for two floating-point values and
#displays the result of the first number divided by the second, 
#with exactly six decimal places displayed in scientific notation. 


float1 = float(input('Enter first floating-point number:   '))

float2 = float(input('Enter second floating-point number:   '))

result = float1/float2

print('the result of the first number divided by the second', format(result,'.6e'))