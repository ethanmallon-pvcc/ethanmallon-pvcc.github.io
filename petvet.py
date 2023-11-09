#Name: Ethan Mallon
#Prog Purpose: This program finds the cost of movie tickets
# Price for one ticket: $10.99
# Sales tac rate: 5.5%

import datetime

############# define global variables #############
# define dog prices
PR_BORD=30
PR_DAPP=35
PR_FLU=48
PR_LEPTO=21
PR_LYME=41
PR_RABIES_D=25
PR_ALL_D=(PR_BORD+PR_DAPP+PR_FLU+PR_LEPTO+PR_LYME+PR_RABIES_D)
PR_CHEW_S=9.99
PR_CHEW_M=11.99
PR_CHEW_L=13.99

# define cat prices
PR_LEUK=35
PR_RHINO=30
PR_RABIES_C=25
PR_ALL_C=(PR_LEUK+PR_RHINO+PR_RABIES_C)
CAT_CHEW=8
#define global variables
pet_name=""
pet_type=""
pet_weight=0
vax_dog=0
vax_cat=0
chew_dog=0
chew_cat=0
dog_total=0
cat_total=0
vax_dog_cost=0
vax_cat_cost=0
chew_cat_cost=0
chew_dog_cost=0
############# define program functions ############
def main():
    more=True

    while more:
        get_user_data()
        if pet_type.upper() == 'D' or pet_type.upper() == 'DOG':
            get_dog_data()
            dog_calc()
            display_dog()
        elif pet_type.upper()=='C' or pet_type.upper()=='CAT':
            get_cat_data()
            cat_calc()
            display_cat()
        else:
            more=False
            print("Invalid response, please try again.")
        askAgain=input("\nWould you like to process another pet (Y or N)?:")
        if askAgain.upper()=="N" or askAgain.upper=="NO":
            more = False
            print("Thank you for trusting PET CARE MEDS with your pet vaccines and medications.")


def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name=input("Pet name: ")
    pet_type=input("Is this pet a dog (D) or cat (C)? ")
    pet_weight=input("Pet weight (in pounds): ")

def get_dog_data():
    global vax_dog,chew_dog
    dog1="\n** Dog Vaccines: \n\t1.Bordatella \n\t2.DAPP \n\t3.Influenza \n\t4.Leptospirosis"
    dog2="\n\t5.Lymes Disease \n\t6.Rabies \n\t7.Full Vaccine Package \n\t8.NONE"
    dogmenu=dog1+dog2
    vax_dog=int(input(dogmenu+"\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all dogs.")
    dheart_yesno=input("would you like to order monthly heartworm medication for "+pet_name+" (Y/N)? ")
    if dheart_yesno.upper()=="Y" or dheart_yesno.upper()=="YES":
        chew_dog=int(input("How any heart worm chews would you like to order? "))
        
def get_cat_data():
    global vax_cat,chew_cat
    cat1="\n** Cat Vaccines: \n\t1.Leukemia \n\t2.Feline Viral Rhinotracheitis \n\t3.Rabies(one year) \n\t4.Full Vaccine Package \n\t5.NONE"
    catmenu=cat1
    vax_cat=int(input(catmenu+"\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all cats.")
    cheart_yesno=input("would you like to order monthly heartworm medication for "+pet_name+" (Y/N)? ")
    if cheart_yesno.upper()=="Y" or cheart_yesno.upper()=="YES":
        chew_cat=int(input("How any heart worm chews would you like to order? "))
        
def dog_calc():
    global vax_dog,chew_dog, dog_total, vax_dog_cost, chew_dog_cost
    if vax_dog==1:
        vax_dog_cost=PR_BORD
    elif vax_dog==2:
        vax_dog_cost=PR_DAPP
    elif vax_dog==3:
        vax_dog_cost=PR_FLU
    elif vax_dog==4:
        vax_dog_cost=PR_LEPTO
    elif vax_dog==5:
        vax_dog_cost=PR_LYME
    elif vax_dog==6:
        vax_dog_cost=PR_RABIES_D
    elif vax_dog==7:
        vax_dog_cost=0.85*PR_ALL_D
    else:
        vax_dog_cost=0
    if chew_dog !=0:
        if pet_weight <25:
                chew_dog_cost=chew_dog*PR_CHEW_S
        elif pet_weight >=26 and pet_weight<50:
                chew_dog_cost=chew_dog*PR_CHEW_M
        elif pet_weight >=51:
                chew_dog_cost=chew_dog*PR_CHEW_L
    dog_total=vax_dog_cost+chew_dog_cost
    

def cat_calc():
    global vax_cat,chew_cat,cat_total,vax_cat_cost, chew_cat_cost
    if vax_cat==1:
        vax_cat_cost=PR_LEUK
    elif vax_cat==2:
        vax_cat_cost=PR_RHINO
    elif vax_cat==3:
        vax_cat_cost=PR_RABIES_C
    elif vax_cat==4:
        vax_cat_cost=0.9*PR_ALL_D
    else:
        vax_cat_cost=0
    if chew_cat !=0:
        chew_cat_cost=chew_cat*CAT_CHEW
    cat_total=vax_cat_cost+chew_cat_cost

def display_dog():
    USDform = '8,.2f'
    line='----------------------'
    print(line)
    print('**** PET CARE MEDS ****')
    print('For our animal friends')
    print(line)
    print('Vaccines     $ ' + format(vax_dog_cost,USDform))
    print('Chews        $ ' + format(chew_dog_cost,USDform))
    print(line)
    print('Total        $ ' + format(dog_total,USDform))
    print(line)
    print(str(datetime.datetime.now()))

def display_cat():
    USDform = '8,.2f'
    line='----------------------'
    print(line)
    print('**** PET CARE MEDS ****')
    print('For our animal friends!')
    print(line)
    print('Vaccines     $ ' + format(vax_cat_cost,USDform))
    print('Chews        $ ' + format(chew_cat_cost,USDform))
    print(line)
    print('Total        $ ' + format(cat_total,USDform))
    print(line)
    print(str(datetime.datetime.now()))

#### call on main program to execute ####
main()


