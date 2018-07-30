
# coding: utf-8

# In[1]:


#Temperature Conversion Program (Fahrenheit to Celsius)

#This program will convert a temperature entered in Fahrenheit
#to the equivalent degrees in Celsius

#program greeting
print('This program will convert degrees Fahrenheit to degrees Celsius')

#get temperature in Fahrenheit
fahren = float(input('Enter degrees Fahrenheit: '))

#calc degrees Celsius
celsius = (fahren - 32) * 5/9

#output degrees Celsius
print(fahren, 'degrees Fahrenheit equals', 
     format(celsius, '.1f'), 'degrees Celsius')


# In[ ]:


#Temperature Conversion Program (Celsius to Fahrenheit)

#This program will convert a temperature entered in Celsius
#to the equivalent degrees in Fahrenheit

#program greeting
print('This program will convert degrees Celsius to degrees Fahrenheit ')

#get temperature in Fahrenheit
celsius = float(input('Enter degrees Celsius: '))

#calc degrees Celsius
fahren = (celsius * 9/5) +32

#output degrees Celsius
print(celsius, 'degrees Celsius equals', 
     format(fahren, '.1f'), 'degrees Fahrenheit')

