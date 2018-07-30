# Stage 1
# Determining the Number of Days in the Month/Leap Years

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

print('\n', month, ',', year, 'has', days_in_month, 'days')