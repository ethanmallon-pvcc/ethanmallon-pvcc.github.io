#Name: Ethan Mallon
#Name: Jay
#Prog Purpose: This program finds the cost of dinners
# Price for adults: $19.95
# Sales tax rate: 6.2%%

import datetime

############# define global variables #############
# define tax rate and prices
SALES_TAX_RATE=0.062
PR_ADULT=19.95
PR_CHILD=11.95
SERVICE=0.1
#define global variables
num_adult=0
num_child=0

subtotal=0
sales_tax=0
total=0
adults=0
children=0
service=0
############# define program functions ############
def main():
    more_meal=True

    while more_meal:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain=input("\nWould you like to order again (Y or N)?:")
        if askAgain.upper()=="N" or askAgain=="n" or askAgain=="No" or askAgain=="no" or askAgain=="NO":
            more_meal = False
            print("Thank you for your order. Enjoy your meal!")


def get_user_data():
    global num_adult
    num_adult=int(input("Number of Adults: "))
    global num_child
    num_child=int(input("Number of Children: "))
    
    
def perform_calculations():
    global subtotal, sales_tax, total, adults, children, service
    adults=(num_adult)*PR_ADULT
    children = num_child*PR_CHILD
    service = (adults+children)*SERVICE
    subtotal = (adults+children+service)
    sales_tax=(subtotal)*SALES_TAX_RATE
    total=adults+children+service+sales_tax

def display_results():
    USDform = '8,.2f'
    line='---------------------------'
    print(line)
    print('**** Branch BBQ Buffet ****')
    print('The Best Homestyle Barbeque')
    print(line)
    print('Adults           $ ' + format(adults,USDform))
    print('Children         $ ' + format(children,USDform))
    print('Service Fee      $ ' + format(service,USDform))
    print('Subtotal         $ ' + format(subtotal,USDform))
    print(line)
    print('Sales Tax        $ '  + format(sales_tax,USDform))
    print('Total            $ ' + format(total,USDform))
    print(line)
    print(str(datetime.datetime.now()))




#### call on main program to execute ####
main()


