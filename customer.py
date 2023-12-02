
#Name: Ethan Mallon
# Name: your name here
# Prog Purpose: This program creates a payroll report

import datetime

cust=[]
######################     define program functions     ######################
def main():
    read_in_cust_file()
    display_cust_list()
        
def read_in_cust_file():
    cust_data=open("cust_data.csv","r")
    cust_in=cust_data.readlines()
    cust_data.close()
    for i in cust_in:
        cust.append(i.split(","))
        
def display_cust_list():
    total=0
    USDform = '6,.2f'
    tab="\t"
    line='----------------------------------------------------------------------------------------------------------------'
    today=str(datetime.datetime.now())
    print(line)
    print('              \t\t\t Customer Sales Report ')
    print(line)
    print('Date:\t\t\t'+today[0:16])
    print(line)
    for i in range(len(cust)):
            owed=float(cust[i][2])*1.1
            total+=owed
            print(cust[i][1] + "    \t"+ cust[i][0] + "\t\t" +format(owed,USDform))
    print(line)
    print('TOTAL AMOUNT:   $' + format(total,USDform))
        
######################      call on main program to execute ######################

main()

