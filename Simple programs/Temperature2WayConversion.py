choice = input('Please Enter Selection:  ')

while choice != 'F' and choice != 'C':
    choice = input('You entered the wrong input data. Please Enter Celcius of Fehrenheit (C or F): ')

if choice == 'F':
    temp = int(input('Please Enter a temparature degree in Fehrenheit:  '))
    converted_temp = (temp - 32) * 5/9
    print('Input Fehrenheit is', temp, '\nthe converted temperature is:  ', 
          format (converted_temp, '.1f'))
else:
    temp = int(input('Please Enter a temparature degree in Celcius:  '))
    converted_temp = (temp * 9/5) + 32
    print('Input Celcius is', temp, '\nthe converted temperature is:  ', 
    format (converted_temp, '.1f'))

         