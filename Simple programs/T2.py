# get month and year
month = int(input('Please write a month (1-12): '))
year = int(input('Please write a year (1800-2099): '))

# determine if leap year
if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
    leap_year = True
else:
    leap_year = False

##################################################################################################3

# Stage 2
# Determining the Day of the Week (using  the day of the week algorithm)

century_digits = year // 100
year_digits = year % 100

# century_digits = int(str(year)[:2])
# year_digits = int(str(year)[-2:])

value = year_digits + (year_digits // 4)

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