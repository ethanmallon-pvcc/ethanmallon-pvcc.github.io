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
SALES_TAX_RATE = .055
PR_SMALL = 19.95
PR_MEDIUM = 12.99
PR_LARGE = 17.99
PR_XLARGE = 21.99
PR_DRINK = 3.99
PR_BREAD = 6.99

# define global variables
num_pizza = 0
num_drink = 0
num_bread = 0
cost_pizza = 0
cost_drink = 0
cost_bread = 0
subtotal = 0
sales_tax = 0
total = 0

######################     define program functions     ######################
def main():
    
    more_food = True

    while more_food:
        get_user_data()
        perform_calculations()
        display_results()
        askAgain = input("\nWould you like to order again (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            more_food = False
            print("Thank you for your order. Enjoy your food")

def get_user_data():
    global num_pizza, num_drink, num_bread, pizza_size
    print("**Palermo Pizzeria**")
    print("\tS. Small		\t$9.99")
    print("\tM. Medium		\t$12.99")
    print("\tL. Large		\t$17.99")
    print("\tX. Extra Large \t\t\t$21.99")
    print("\tN. NONE")
    pizza_size = input("\nWhat size pizza(s) would you like to order?: ")
    if pizza_size.upper() == 'N' or pizza_size.upper() == 'NONE':
        num_pizza = 0
    else:
        num_pizza = int(input("Number of pizzas: "))
    drink_yesno = input("Would you like to add drinks for $3.99 each (Y/N)?: ")
    if drink_yesno.upper() == "Y" or drink_yesno.upper() == "YES":
        num_drink =int(input("How many drinks would you like to add to your order?: "))
    bread_yesno = input("Would you like to add breadsticks to your order for $6.99 each (Y/N)?: ")
    if bread_yesno.upper() == "Y" or bread_yesno.upper() == "YES":
        num_bread =int(input("How many orders of breadsticks would you like to add to your order?: "))

def perform_calculations():
    global cost_pizza ,cost_drink, cost_bread, subtotal, sales_tax, total
    if pizza_size.upper() == 'S' or pizza_size.upper() == 'SMALL':
        cost_pizza = num_pizza*PR_SMALL
    elif pizza_size.upper() == 'M' or pizza_size.upper() == 'MEDIUM':
        cost_pizza = num_pizza*PR_MEDIUM
    elif pizza_size.upper() == 'L' or pizza_size.upper() == 'LARGE':
        cost_pizza = num_pizza*PR_LARGE
    elif pizza_size.upper() == 'X' or pizza_size.upper()=='EXTRA LARGE':
        cost_pizza = num_pizza*PR_XLARGE
    else:
        cost_pizza = 0
    cost_drink = num_drink*PR_DRINK
    cost_bread = num_bread*PR_BREAD
    subtotal = cost_pizza+cost_drink+cost_bread
    sales_tax = subtotal*SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    moneyf = '8,.2f'
    line='---------------------------------'
    print(line)
    print('******* Palermo Pizzeria ********')
    print('*** Authentic Italian Cuisine ***')
    print(line)
    print(str(num_pizza)+' Pizza(s)         \t$'+format(cost_pizza, moneyf))
    print('Drinks           \t$'+format(cost_drink, moneyf))
    print('Breadsticks      \t$'+format(cost_bread, moneyf))
    print(line)
    print('Subtotal         \t$'+format(subtotal, moneyf))
    print('Sales Tax        \t$'+format(sales_tax, moneyf))
    print('Total            \t$'+format(total, moneyf))
    print(line)
    print(str(datetime.datetime.now()))
    
######################      call on main program to execute ######################

main()

