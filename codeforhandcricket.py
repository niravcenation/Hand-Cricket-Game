import csv
import sys

def main():
    menu()

def menu():
    print("**WELCOME**")
    print()

    choice = input("""
                      A: Start Playing Game
                      B: Instructions
                      C: Quit
                      please enter your choice:""")
    if choice=="A" or choice=="a":
        import mainmenu
        mainmenu.start()
    elif choice=="B" or choice=="b":
        import instruction
        instruction.help()
    elif choice=="c" or choice=="C":
        sys.exit
    else:
        print("You must enter A or B")
        print("Please try again")

main()




