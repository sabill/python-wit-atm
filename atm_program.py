# WOMAN IN Tech
# Sabila Hadinnisa, dec 2020

import random
import datetime
from customer import Customer

while True:
    option = int(input('Welcome to ATM Woman In Tech\n1. Create an account\n2. Log into account\n0. Exit\n'))
    if option == 1:
        object1 = Customer(random.randint(10**15,9999999999999999), random.randint(10**5,999999), 0)
        print('Your card has been created')
        print('Your card number:')
        print(object1.id)
        print('Your card PIN:')
        print(object1.defaultPin)
    elif option == 2:
        login = int(input('Enter your card number:\n'))
        if login == object1.id:
            trial = 3
            while trial > 0:
                my_pin = int(input('Enter your PIN:\n'))
                if my_pin == object1.defaultPin:
                    print('You have successfully logged in!')
                    while True:
                        print('1. Balance')
                        print('2. Debet')
                        print('3. Save money')
                        print('4. Change PIN')
                        print('5. Log out')
                        print('0. Exit')
                        option2 = int(input(''))
                        if option2 == 1:
                            print('Your balance: '+str(object1.checkBalance()))
                        elif option2 == 2:
                            debt = int(input('Enter debit amount: '))
                            print(object1.withdrawBalance(debt))      
                            print('Remaining balance: ', object1.defaultBalance)
                        elif option2 == 3:
                            add = int(input('Enter save amount: '))
                            print(object1.depositBalance(add))
                            print('Remaining balance: ', object1.defaultBalance)
                        elif option2 == 4:
                            new_pin = int(input('Enter new PIN: '))
                            curr_pin = int(input('Enter your current PIN :'))
                            if curr_pin == object1.defaultPin:
                                object1.defaultPin = curr_pin
                                print('Your PIN successly changed..')
                            else: print('Error, you enter wrong PIN!')
                        elif option2 == 5:
                            print('Successly log out..')
                            print('Record number: ', random.randint(10**5,10**6))
                            print('Date: ', datetime.datetime.now())
                            print('Balance: ', object1.defaultBalance)
                            exit()
                        elif option2 == 0:
                            exit()
                        else : print('Error! Please enter a valid option..\n')
                        
                else:
                    print('Error! You enter wrong PIN, please try again..')
                    trial -= 1
                    if(trial == 0):
                        print('Error, please take your card and try again..')

        else: print('Your card number wasn\'t registered, please try again!' )    
    elif option == 0:
        print('Thank you for using ATM :))')
        exit()
    else: print('Select available option!')        