#Develop a program to display a calender month for any given month between January 1800 and December 2099.

#Develop a program that promps the user for a given month (and year for February), 
#and display how many days are in the month.

year = int(input('Please write a year (1800-2099): '))
month = int(input('Please write a month (1-12): '))
   
if month in (1 ,3 ,5 ,7 ,8 ,10 ,12):
    days_in_month = 31 
elif month in (3, 6 ,9 ,11):
    days_in_month = 30 
elif month in (2):
    year = int(input('Enter year: '))
    if ((year % 4 == 0) and not(year % 100 == 0)) or ((year % 4 == 0) and (year % 400 == 0)):       
        days_in_month = 29    
    else: 
        days_in_month = 28 
else:
    print ('Invalid input')
    
    
#This program allows the user to enter the year, month and day, and as the output, the program determines the day of the week    
centry_digits = int(str(year)[:2])
print(int(str(year)[:2]))
year_digits = int(str(year)[-2:])
print(int(str(year)[-2:]))
value = year_digits + (year_digits//4)

if centry_digits == 18:
    value = value + 2
if centry_digits == 20:
    value = value + 6
    
if (month == 1) and  not ((year % 4 == 0) and not(year % 100 == 0)) or ((year % 4 == 0) and (year % 400 == 0)):
    value = value + 1
elif (month == 2) and ((year % 4 == 0) and not(year % 100 == 0)) or ((year % 4 == 0) and (year % 400 == 0)):
    value = value + 3
elif (month == 2) and not ((year % 4 == 0) and not(year % 100 == 0)) or ((year % 4 == 0) and (year % 400 == 0)):
    value = value + 4
elif (month == 3) or (month == 11):
    value = value + 4
elif (month == 4) or (month == 7):
    value = value + 0
elif (month == 5):
    value = value + 2
elif (month == 6):
    value = value + 5
elif (month == 8):
    value = value + 3
elif (month == 10):
    value = value + 1
elif (month == 9) or (month == 12):
    value = value + 6
else:
    print('Invalid input 1.')
    
value = (value + 1) %  7


if value == 1:
    day_of_the_week = 1
elif value == 2:
    day_of_the_week = 2
elif value == 3:
    day_of_the_week = 3 
elif value == 4:
    day_of_the_week = 4
elif value == 5:
    day_of_the_week = 5
elif value == 6:
    day_of_the_week = 6
elif value == 0:
    day_of_the_week = 7
else:
    print('Invalid input 2.')
    
    
if month == 1:
    Month = 'January'
if month == 2:
    Month = 'February '    
if month == 3:
    Month = 'March'
if month == 4:
    Month = 'April'    
if month == 5:
    Month = 'May'    
if month == 6:
    Month = 'June'    
if month == 7:
    Month = 'July'    
if month == 8:
    Month = 'August '
if month == 9:
    Month = 'September'    
if month == 10:
    Month = 'October '
if month == 11:
    Month = 'November'    
if month == 12:
    Month = 'December'    
    
    
    
#Display calendar for the month

#print(days_in_month)
#print(day_of_the_week)


#Heading
print( Month, year)
print('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')

current_col = 1 
current_day = 1

#starting column
if value == 0:
    starting_col = 7
elif value <= 6:
    starting_col = value

#print spaces before the 1st day of the month
while current_col < starting_col:
    print(format(' ','4'), end = '')
    current_col = current_col + 1

#print days
while current_day <= days_in_month:
    if current_col > 7:
        current_col = 1
        print()
    print(format(str(current_day), '4'), end = '')
    current_day = current_day + 1
    current_col = current_col + 1
        



#Program Implementation and Testing. 
#Introduction to Computer Science Using Python: A Computational Problem-Solving Focus. p.107 

   












    
    
