
#Name: Ethan Mallon
# Name: your name here
# Prog Purpose: This program creates a payroll report

import datetime

############## LISTS of data ############
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
     "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

grosspay=[]
fedtax=[]
statetax=[]
socialsec=[]
medicare=[]
retire=[]
netpay=[]
grosstotal=0
nettotal=0
##TUPLES##
#           C   S   J   M
# indexes   0   1   2   3
PAY_RATE=(16.50,15.75,15.75,19.50)
#           fed  state  soc med ret
# indexes   0    1      2   3   4
DED_RATE=(.12,.03,.062,.0145,.04)
######################     define program functions     ######################
def main():
    perform_calculations()
    display_results()
        
def perform_calculations():
    global grosstotal, nettotal
    for i in range(num_emps):
        if job[i]=="C":
            pay=hours[i]*PAY_RATE[0]
        elif job[i] == "S":
            pay=hours[i]*PAY_RATE[1]
        elif job[i] == "J":
            pay=hours[i]*PAY_RATE[2]
        else:
            pay=hours[i]*PAY_RATE[3]
        fed=pay*DED_RATE[0]
        state=pay*DED_RATE[1]
        soc=pay*DED_RATE[2]
        med=pay*DED_RATE[3]
        ret=pay*DED_RATE[4]
        net=pay-fed-state-soc-med-ret
        grosstotal+=pay
        nettotal+=net
        grosspay.append(pay)
        fedtax.append(fed)
        statetax.append(state)
        socialsec.append(soc)
        medicare.append(med)
        retire.append(ret)
        netpay.append(net)
        
        
def display_results():
    USDform = '11,.2f'
    tab="\t"
    line='----------------------------------------------------------------------------------------------------------------'
    today=str(datetime.datetime.now())
    print(line)
    print('              \t\t\t************* FRESH FOODS MARKET *************')
    print('              \t\t\t************ WEEKLY PAYROLL REPORT ***********')
    print(line)
    print('Date:\t\t\t'+today[0:16])
    print(line)
    print('\nEmp.' + tab + tab + tab + 'Code' + tab + "     Gross" + tab + " Federal" + "    State" +  "      Social" + "      Medicare" + "  Retire" + "    Net")
    print(line)

    for i in range(num_emps):
            data1=emp[i] + tab + job[i] + tab + format(grosspay[i],USDform) + format(fedtax[i],USDform)+ format(statetax[i],USDform) + format(socialsec[i],USDform) + format(medicare[i],USDform) + format(retire[i],USDform)+ format(netpay[i],USDform)
            print(data1)
    print(line)
    print('TOTAL GROSS:  \t' + tab + tab + format(grosstotal,USDform))
    print('TOTAL NET  :  \t' + tab + tab + format(nettotal,USDform))

    
######################      call on main program to execute ######################

main()

