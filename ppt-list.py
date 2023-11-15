
#Name: Ethan Mallon
#Prog Purpose: This program finds the due personal property tax from vehicle information
import datetime

######################     define global variables      ######################
# define tax rate and prices
PROP_TAX_RATE = .042
RELIEF=0.33

# define global variables
vehicle=["2019 Volvo ",
         "2018 Toyota",
         "2022 Kia   ",
         "2020 Ford  ",
         "2023 Honda ",
         "2019 Lexus "]
value=[13000,10200,17000,21000,28000,16700]
eligible=["Y","Y","N","Y","N","Y"]
owner=["Brand, Debra      ",
       "Smith, Carter     ",
       "Johnson, Bradley  ",
       "Garcia, Jennifer  ",
       "Henderson, Leticia",
       "White, Danielle   "]
owed=[]
num_vehicle=len(vehicle)
tax_due=0
total=0

######################     define program functions     ######################
def main():
    perform_calculations()
    display_results()
        
def perform_calculations():
    global total, eligible, owed
    for i in range(num_vehicle):
        tax_due=(value[i]*PROP_TAX_RATE)/2
        if eligible[i].upper()=="Y":
            tax_due=tax_due*0.67
        owed.append(tax_due)
        total=total+tax_due
    
def display_results():
    USDform = '11,.2f'
    tab="\t"
    line='------------------------------------------------------------------------'
    today=str(datetime.datetime.now())
    print(line)
    print('              ********** Personal Property Tax **********')
    print("              ************ Semiannual Amount ************")
    print(line)
    print('Date:\t\t\t'+today[0:16])
    print(line)
    print('\nNAME' + tab + tab + tab + '  VEHICLE VALUE' + tab + tab + "RELIEF" + tab + "   TAX DUE")
    print(line)

    for i in range(num_vehicle):
            dataline1=owner[i] + tab + format(value[i],USDform) + tab
            dataline2= tab + eligible[i] + tab + format(owed[i],USDform)
            print(dataline1+dataline2)
    print(line)
    print('TOTAL DUE:  \t' + tab + tab +tab + tab + tab + format(total,USDform))
    
    
######################      call on main program to execute ######################

main()

