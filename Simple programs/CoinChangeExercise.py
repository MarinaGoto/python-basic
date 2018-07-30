#An exercise for children learning to count change.
#It displays a random value between 1 and 99 cents, and 
#asks the user to enter a set of coins that sums exactly to the amount shown.

looping = True
while looping:
    
    amount = int(input('Please enter an total amount (1-99): '))
    total = 0

    while total < amount: 
        choice = int(input('Please choose between 1 or 5 or 10 or 20:   '))
        while choice not in (1, 5, 10, 20):
            print('Invalid input!')
            choice = int(input('Please choose between 1 or 5 or 10 or 20:   '))
              
        total = total + choice
        print('Only', amount - total, 'amount left')
                  
    if total == amount:
        print(amount - total, 'amount left')
        print('you won!')
    else:
        print('You lost')
                  
    decision = input('Do you want to play the game again (y or n)?:  ')
    while decision not in ('y','n'):
                  decision = input('Do you want to play the game again? (y or n):   ')
    if decision == 'y':
                  looping = True
    else:
                  looping = False              
           
