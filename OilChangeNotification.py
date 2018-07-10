#Program that calculates the amount of oil in the bank and
#gives early warning if the user has driven more then 7000 miles but less then 7500 miles and
#calculets in what amount of mile the user shall change the bank
#gives warning if the user has driven more then 7500 mile

ml = int(input('How many miles did you travel before the last filing of the oil bank?  '))
mlNew = int(input('How many miles have you traveled till now?  '))

amount = mlNew - ml

last_ml= 7500 - amount

if amount >= 7000 and amount < 7500:
    print('Early warning. You must fill the oil bank in', last_ml ,'ml')    
elif amount >= 7500  :
    print('Warning! Fill the oil bank now!')
else:
    print('All right! Continue to go!')
    