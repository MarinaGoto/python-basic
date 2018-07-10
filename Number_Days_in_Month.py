#Develop a program that promps the user for a given month (and year for February), 
#and display how many days are in the month.


month = input('Enter month: ')
    
if month in ('January' ,'March' ,'May' ,'July' ,'August' ,'October' ,'December'):
    print('31 days')
elif month in ('April', 'June' ,'September' ,'November'):
    print('30 days')
elif month in ('February'):
    year = int(input('Enter year: '))
    if ((year % 4 == 0) and not(year % 100 == 0)) or ((year % 4 == 0) and (year % 400 == 0)):       
        print('29 days')    
    else: 
        print('28 days')  
else:
    print ('Invalid input')


         
         
         
