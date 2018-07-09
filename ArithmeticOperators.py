#Write a Python program that allows the user to enter two integer values, and 
#displays the results when each of the following arithmetic operators are applied.

#All floating-point results should be displayed with two decimal places of accuracy. 
#In addition, all values should be displayed with commas where appropriate. 

Int1 = int(input('Please write the first integer:   '))
Int2 = int(input('Please write the second integer:   '))

Add = Int1 + Int2
Subt = Int1 - Int2
Mult = Int1 * Int2
Divis = Int1 / Int2
Floor_Divis = Int1 // Int2
Mod = Int1 % Int2
Exp = Int1 ** Int2

print ('Addition', format(Add, ',.2f'))
print ('Subtraction', format(Subt, ',.2f'))
print ('Multiplication', format(Mult, ',.2f'))
print ('Floor Division ', format(Floor_Divis, ',.2f'))
print ('Modulus', format(Mod, ',.2f'))
print ('Exponent', format(Exp, ',.2f'))