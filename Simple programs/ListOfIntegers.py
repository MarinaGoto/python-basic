#Write a Python program that prompts the user for a list of integers, 
#stores in another list only those values
#between 1–100, and displays the resulting list. 


num1 = int(input('Please write the 1st number:   '))
num2 = int(input('Please write the 2st number:   '))
num3 = int(input('Please write the 3st number:   '))


list1 = [ ]
list1.append( num1)
list1.append( num2)
list1.append( num3)

list2 = [ ]

for i in list1:
    if i in range(1, 101):
        list2.append(i)
print(list2)