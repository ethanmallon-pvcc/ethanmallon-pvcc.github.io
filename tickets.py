#Name: Ethan Mallon
#Prog Purpose: This program finds the cost of movie tickets
# Price for one ticket: $10.99
# Sales tac rate: 5.5%

import datetime

############# define global variables #############
# define tax rate and prices
SALES_TAX_RATE=0.055
PR_TICKET=10.99
PR_PCORN=12.99
PR_DRINK=4.99
#define global variables
num_tickets=0
num_pcorn=0
num_drink=0
subtotal=0
sales_tax=0
total=0
tickets=0
popcorn=0
drinks=0
############# define program functions ############
def main():
    more_tickets=True

    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain=input("\nWould you like to order again (Y or N)?:")
        if askAgain.upper()=="N" or askAgain=="n" or askAgain=="No" or askAgain=="no" or askAgain=="NO":
            more_tickets = False
            print("Thank you for your order. Enjoy your movie!")


def get_user_data():
    global num_tickets
    num_tickets=int(input("Number of Movie Tickets: "))
    global num_pcorn
    num_pcorn=int(input("Number of Popcorn Buckets: "))
    global num_drink
    num_drink=int(input("Number of Drinks: "))
    
def perform_calculations():
    global subtotal, sales_tax, total, tickets, popcorn, drinks
    tickets=(num_tickets)*PR_TICKET
    popcorn = num_pcorn*PR_PCORN
    drinks = num_drink*PR_DRINK
    sales_tax=(tickets+popcorn+drinks)*SALES_TAX_RATE
    total=tickets+popcorn+drinks+sales_tax

def display_results():
    USDform = '8,.2f'
    line='-----------------------------'
    print(line)
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print(line)
    print('Tickets     $ ' + format(tickets,USDform))
    print('Popcorn     $ ' + format(popcorn,USDform))
    print('Drinks      $ ' + format(drinks,USDform))
    print(line)
    print('Sales Tax   $ '  + format(sales_tax,USDform))
    print('Total       $ ' + format(total,USDform))
    print(line)
    print(str(datetime.datetime.now()))




#### call on main program to execute ####
main()


