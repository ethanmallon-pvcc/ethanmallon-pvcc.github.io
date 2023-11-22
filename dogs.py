
#Name: Ethan Mallon
#Prog Purpose: This program demonstrates the operations and ways to manipulate a Python List
import datetime

######################     define global variables      ######################

# define global variables
dogs=["Sadie","Molly","Ella","Milo","Buddy","Rocky","Annabelle","Gonzo", "Eli", "Emmett", "Mimzy", "Diego"]

dogs2=[]


######################     define program functions     ######################
def main():
    amt=len(dogs)
    print("\nNumber of dogs in the list: " + str(amt))
    print("\nOriginal list of dog names: ")
    print(dogs)

    dogs.reverse()
    print("\nList from last to first: ")
    print(dogs)

    dogs.sort()
    print("\nAlphabetical list: ")
    print(dogs)

    dogs.sort(reverse=True)
    print("\nList in reverse alphabetical order: ")
    print(dogs)

    dogs.append("Ranger")
    print("\nAdd a dog to the end of the list: ")
    print(dogs)

    doggy=dogs.pop(0)
    print("\nPop(remove) a dog from the front of the list: ")
    print(dogs)
    print(doggy + " was removed from the front of the list.")

    another=dogs.pop(3)
    print("\nNote: Position numbers in a list befin with 0, not 1.")
    print("\nRemove the dog in position 3 (the fourth dog): ")
    print(dogs)
    print(another + " was removed from position 3 of the list.")
    
    dogs.remove("Annabelle")
    print("\nRemove a dog by name rather than position: ")
    print(dogs)

    dogs2=dogs
    print("\nA list can be copied into another list by setting one equal to the other: ")
    print(dogs)
    print(dogs2)

    print("\nUse a FOR loop to give each dog in the list the same last name: ")
    for i in range(len(dogs)):
            dogs[i]=dogs[i] + " Mallon"
    print(dogs)

    
######################      call on main program to execute ######################

main()

