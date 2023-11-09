#Name: Loren Lemarr
#Name: Ethan Mallon
#Prog Purpose: This program finds the cost of ordering from Pslermo Pizza
#   Price for Small: $9.99
#   price for Medium: $12.99
#   price for Large: $17.99
#   price for Extra Large: $21.99
#   price for Drink: $3.99
#   price for Breadsticks: $6.99
#   Sales tax rate: 5.5%

import datetime

######################     define global variables      ######################
# define tax rate and prices
PROP_TAX_RATE = .042
RELIEF=0.33

# define global variables
full_amt_owed = 0
total = 0
eligible=""

######################     define program functions     ######################
def main():
    
    more_vehicles = True

    while more_vehicles:
        get_user_data()
        perform_calculations()
        display_results()
        askAgain = input("\nDo you have another vehicle to input(Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            more_vehicles = False
            print("Payment is due within 3 months of the completion of this form.")

def get_user_data():
    global assess_value, eligible
    
    assess_value = int(input("Enter the assessed value of the vehicle (do not include commas): "))
    eligible=input("Is this vehicle eligible for relief (Y/N)? ")

def perform_calculations():
    global full_amt_owed,relief, total, eligible, amt_semiann, RELIEF
    
    full_amt_owed=assess_value*PROP_TAX_RATE
    amt_semiann=full_amt_owed/2

    if eligible.upper()=="Y":
        relief=RELIEF*(amt_semiann)
    else:
        relief=0
    total = (amt_semiann)-relief
    
def display_results():
    USDform = '11,.2f'
    line='-------------------------------------------'
    today=str(datetime.datetime.now())
    print(line)
    print('********** Personal Property Tax **********')
    print("************ Semiannual Amount ************")
    print(line)
    print('Date: \t\t\t'+today[0:16])
    print(line)
    print('Assessed Vehicle Value: $'+format(assess_value, USDform))
    print(line)
    print('Owed: \t\t\t$'+format(amt_semiann, USDform))
    print(line)
    print('Relief: \t\t$'+format(relief, USDform))
    print(line)
    print('Total Due: \t\t$'+format(total,USDform))
    print(line)
    
    
######################      call on main program to execute ######################

main()

