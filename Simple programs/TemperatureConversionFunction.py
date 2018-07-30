#this function takes two input data. 
#The first parameter records the temperature.
#The second parameter records the selection (either C: Celcius or F: Fehrenheit)



#First design choice  


def convert(temperature, selection):
    if selection == 'F':
        converted_temp = (temperature - 32) * 5/9
       
    else:
        converted_temp = (temperature * 9/5) + 32
       
    return converted_temp
    
    
###############################################################################################3

choice = input('Please Enter type of the temperature that you want to convert in Celcius or Fehrenheit (C or F):  ')

while choice != 'F' and choice != 'C':
    choice = input('You entered the wrong input data. Please Enter Celcius or Fehrenheit (C or F): ')
    
    
temp = int(input('Please Enter a temperature degree:  '))

if choice == 'F':
     print('Input Fehrenheit is', temp, '\nthe converted temperature is:  ', 
          format (convert(temp, choice), '.1f'))
else:
     print('Input Celcius is', temp, '\nthe converted temperature is:  ', 
          format (convert(temp, choice), '.1f'))
        
        
#Second design choice        
        
def convert(temperature, selection):
    if selection == 'F':
        converted_temp = (temperature - 32) * 5/9
        print('Input Fehrenheit is', temperature, '\nthe converted temperature is:  ', 
          format (converted_temp, '.1f'))
    else:
        converted_temp = (temperature * 9/5) + 32
        print('Input Celcius is', temperature, '\nthe converted temperature is:  ', 
          format (converted_temp, '.1f'))
    return temperature
    
    
###############################################################################################3

choice = input('Please Enter Celcius of Fehrenheit (C or F):  ')

while choice != 'F' and choice != 'C':
    choice = input('You entered the wrong input data. Please Enter Celcius of Fehrenheit (C or F): ')
    
    
temp = int(input('Please Enter a temperature degree:  '))

convert(temp, choice) 


         