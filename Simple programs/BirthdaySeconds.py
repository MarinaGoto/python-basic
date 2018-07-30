import datetime

print('Calculate how many seconds have you lived')

your_year = int(input('Please enter your birth year: '))
your_month = int(input('Please enter your birth month (1-12): '))
your_day = int(input('Please enter your birth day (1-31): '))

current_year = datetime.date.today().year
current_month = datetime.date.today().month
current_day = datetime.date.today().day

print('your birhdate is ', your_day, your_month , your_year)
print('current time is ', current_day, current_month , current_year)

#total days of a year * total seconds per day = total seconds per year
#avg_secs_year = 365.25 * (24*60*60)

#total second per day
secs_day = 24*60*60

#average seconds per year
avg_secs_year = ((secs_day * 365 * 4) + secs_day) // 4

#averge seconds per month
avg_secs_month = avg_secs_year // 12


total_secs_to_current_year = (current_year - 1970) * avg_secs_year
total_extra_secs_to_current_month = (current_month - 1) * avg_secs_month
total_extra_second_to_current_day = current_day * secs_day

total_secs_to_current_time = total_secs_to_current_year + \
                             total_extra_secs_to_current_month + \
                             total_extra_second_to_current_day 

#print('total secs to current time' , total_secs_to_current_time)


#Calculate how many seconds have you lived



total_secs_to_your_year =  (your_year - 1970) * avg_secs_year
total_extra_secs_to_your_month = (your_month - 1)  * avg_secs_month
total_extra_secs_to_your_day = your_day * secs_day


total_secs_to_your_time = total_secs_to_your_year + \
                             total_extra_secs_to_your_month + \
                             total_extra_secs_to_your_day 



total_second_up_to_your_birthdate = total_secs_to_current_time - total_secs_to_your_time

print('total second up to your birthdate' , total_second_up_to_your_birthdate )
                                  
print('error persentage:',(total_secs_to_current_time - 1530790392)/ 1530790392 * 100, '%')                                  






