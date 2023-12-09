
#Name: Ethan Mallon
#Prog Purpose: To import data from a .csv and then export said data in the form of an HTML. This will serve as a portion of my final exam grade.

import datetime


out = 'emerald.html'
#define global variables
roomtotal=0
nights=[]
room=[]
guest=[]
roomcost=[195,250,350]
tax=[0.065,0.1125]
grandtotal=0
salestax=0
occupancy=0
total=0
f=open(out, 'w')


##define program functions
def main():
    read_in_guest_file()
    open_out()
    perform_calculations()
    display_results()
            
def read_in_guest_file():
    guest_data=open("emerald.csv","r")
    guest_in=guest_data.readlines()
    guest_data.close()
    for i in guest_in:
        guest.append(i.split(","))
        
def open_out():        
    global f
    f = open(out, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: center} </style> </head>\n')
    f.write('<body style ="background-color: #f9fffa; background-image: url(em-wp.jpg);text-align: center; color: #f8dd61;">\n')
    

def perform_calculations():
    global grandtotal
    grandtotal=0
    for i in range(len(guest)):
            room=str(guest[i][2])
            nights=int(guest[i][3])
            if room=="SR":
                roomtotal=roomcost[0]*nights
            elif room=="DR":
                roomtotal=roomcost[1]*nights
            else:
                roomtotal=roomcost[2]*nights
            
            salestax=roomtotal*tax[0]
            occupancy=roomtotal*tax[1]
            total=roomtotal+salestax+occupancy
            grandtotal+=total
        

            guest[i].append(roomtotal)
            guest[i].append(salestax)
            guest[i].append(occupancy)
            guest[i].append(total)
            
def display_results():
    global f

    
    USDform="8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    td = '</td><td>'
    tdb='</td><td style="font-weight:bold;">'
    tdd = '</td><td style="text-align: right;">'
    endtr = '</td></tr>\n'
    sp = " "

    f.write('\n<table border="5"   style ="background-color: #f9fffa; color: #3f301d; width: 60%; border-color: #1a6128; font-family: Arial, Helvetica, sans-serif; margin: auto;">\n')            
    f.write('<tr><td colspan = 7>\n')
    f.write('<h1 style ="text-align:center; font-weight:bold;">Emerald Beach Hotel & Resort</h1></td></tr>')

    f.write('<tr><td style="font-weight: bold;">Last Name' +  tdb + 'First Name' +  tdb + '# Nights' +  tdb + 'Subtotal' +  tdb + 'Sales Tax' +  tdb + 'Occ. Tax' +  tdb + 'Total' + endtr)

    for i in range(len(guest)):
        f.write(tr + str(guest[i][0]) + td + str(guest[i][1]) + td + str(guest[i][3]) + tdd + format(guest[i][4],USDform) +tdd+  format(guest[i][5],USDform) +tdd+ format(guest[i][6],USDform) +tdd + format(guest[i][7],USDform) + endtr)

    f.write("<tr><td colspan= '7' style='text-align: right; font-weight:bold; '>Grand Total: $"+ format(grandtotal, USDform) +endtr)
    f.write('<tr><td colspan= "7" style="text-align: right; font-weight:bold;">Date/Time: ')
    f.write(day_time)
    f.write(endtr)
    f.write('</table><br />')
    print('Open ' + out + ' to view data.')

    f.write("</body></html>")
    f.close()            
##call on main program to execute##
main()
