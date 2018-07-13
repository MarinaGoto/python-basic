# Program to display a calendar month for any given month between January 1800 and December 2099.


# We develop and test the program in three stages.

#     Stage 1 — Determine the Number of Days in the Month/Leap Years
# We implement and test the code that determines, for a given month and year,
# the number of days in the month and whether the year is a leap year or not.

#    Stage 2 — Determine the Day of the Week
# The code determines the day of the week
# for the first day of a given month and year

#    Stage 3 — Display the Calendar Month

############################################################################################

# Stage 1
# Determining the Number of Days in the Month/Leap Years

# program greeting
print('This program will display a calender month between January 1800 and December 2099.')

# get month and year
month = int(input('Please write a month (1-12): '))
year = int(input('Please write a year (1800-2099): '))

# determine if leap year
if(year % 4 == 0) and (not(year % 100 == 0) or (year % 400 == 0)):
    leap_year = True
else:
    leap_year = False

# determine number of days in month
if month in (1, 3, 5, 7, 8, 10, 12):
    days_in_month = 31 
elif month in (4, 6, 9, 11):
    days_in_month = 30 
elif leap_year:  # February
    days_in_month = 29
else:
    days_in_month = 28

############################################################################################

# Stage 2
# Determining the Day of the Week (using  the day of the week algorithm)

century_digits = year//100
year_digits = year % 100

# century_digits = int(str(year)[:2])
# year_digits = int(str(year)[-2:])

value = year_digits + (year_digits//4)

if century_digits == 18:
    value = value + 2
if century_digits == 20:
    value = value + 6
    
if (month == 1) and not leap_year:
    value = value + 1
elif month == 2:
    if leap_year:
        value = value + 3
    else:
        value = value + 4
elif (month == 3) or (month == 11):
    value = value + 4
elif month == 5:
    value = value + 2
elif month == 6:
    value = value + 5
elif month == 8:
    value = value + 3
elif month == 10:
    value = value + 1
elif (month == 9) or (month == 12):
    value = value + 6

#  for this program, we will need to determine only the day of the week
#  for the first day of any given month
#  the day value in the day of the week algorithm is hard-coded to 1
day_of_the_week = (value + 1) % 7

# determine week day name
if day_of_the_week == 1:
    dayName = 'Sunday'
elif day_of_the_week == 2:
    dayName = 'Monday'
elif day_of_the_week == 3:
    dayName = 'Tuesday'
elif day_of_the_week == 4:
    dayName = 'Wednesday'
elif day_of_the_week == 5:
    dayName = 'Thursday'
elif day_of_the_week == 6:
    dayName = 'Friday'
elif day_of_the_week == 0:
    dayName = 'Saturday'

# determine month name
if month == 1:
    monthName = 'January'
if month == 2:
    monthName = 'February '
if month == 3:
    monthName = 'March'
if month == 4:
    monthName = 'April'
if month == 5:
    monthName = 'May'
if month == 6:
    monthName = 'June'
if month == 7:
    monthName = 'July'
if month == 8:
    monthName = 'August '
if month == 9:
    monthName = 'September'
if month == 10:
    monthName = 'October '
if month == 11:
    monthName = 'November'
if month == 12:
    monthName = 'December'

# display results
print('The first day of ', monthName, 'is', dayName)

############################################################################################

# Stage 3
# Displaying the Calendar Month

# Display month and year heading
print('\n', ' ', monthName, year)

# Display week days names
print('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')

current_col = 1 
current_day = 1
starting_col = 1

# determine starting column
if day_of_the_week == 0:
    starting_col = 7
elif day_of_the_week <= 6:
    starting_col = day_of_the_week

# print spaces before the 1st day of the month
while current_col < starting_col:
    print(format(' ', '4'), end='')
    current_col = current_col + 1

# print days
while current_day <= days_in_month:
    if current_col > 7:
        current_col = 1
        print()
    print(format(str(current_day), '4'), end='')
    current_day = current_day + 1
    current_col = current_col + 1


# Introduction to Computer Science Using Python by Charles Dierbach. p.107
