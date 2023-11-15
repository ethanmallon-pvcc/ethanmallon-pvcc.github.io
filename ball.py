#Name: Ethan Mallon
#Prog Purpose: This program is an example of python Tuple code which does not rely on user input to determine an answer.
#The effects of a Tuple can be achieved through the use of a Python list.
# Format Note: Tuples use parentheses, Lists use brackets

import random

############# define global variables #############
responses=("As i see it, yes.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","It is certain.","It is decidedly so.","Most likely.","My reply is no.","My sources say no.","The outlook is good.","The outlook doesn't look good.","Hazy reply, try again.","Signs point to yes.","Doubtful.","Without a doubt.", "Yes.","Definitely.","You may rely on it.")
############# define program functions ############
def main():
    print("I am the hailed Ball of 8, any question I can answer; if it's 'yes' or 'no'.")
    more_quest=True

    while more_quest:
        answer=random.choice(responses)
        quest=input("\nWhat do you wish to know? Does it regard a lover? Something precious? Tell me!\n")
        print("\nI see...that is a sufficent question, though rather boring, no?")
        print("\nBut I am a Ball of my word, here is the answer to that which you seek to know: \n"+answer)
        print("\n...well? Satisfied?")
        askAgain=input("\nAny more questions for me?\n")
        if askAgain.upper()=="N" or askAgain.upper()=="NO":
            more_quest = False
            print("\nVery well...I hope the answer was worth it. You know where to find me should you seek any more.")



#### call on main program to execute ####
main()


