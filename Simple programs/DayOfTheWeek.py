#This program allows the user to enter the year, month and day, and as the output, the program determines the day of the week


year = int(input('Please write a year: '))
month = int(input('Please write a month (1-12): '))
day = int(input('Please write a day: '))


centry_digits = int(str(year)[:2])

year_digits = int(str(year)[-2:])

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
    print('Sunday')
elif value == 2:
    print('Monday')
elif value == 3:
    print('Tuesday')
elif value == 4:
    print('Wednesday')
elif value == 5:
    print('Thursday')
elif value == 6:
    print('Friday')
elif value == 0:
    print('Saturday')
else:
    print('Invalid input 2.')
 