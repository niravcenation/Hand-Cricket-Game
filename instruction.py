import csv 
import sys

def main():
    help()

def help():
    print("""                                   -------INSTRUCTIONS-------
    
                1. Give start playing command
                2. Enter your name and Select in which mode you want to play
                3. Select even/odd for toss and accordingly select random number [1-10]
                4. Select whether you want to do batting or bowling
                5. Enter the numbrer of the overs you want to play
                6. Then enter random numbers betwwen the given range 
                    if player's batting is going on than his scored will be counted according to the numbers entered by the player and 
                    in bowling user has to only enter the random number,
                    and if same number appears for both the players than the batsman will be out 
                                                                                                     """)
    quit = input("    Write back command to return to the menu  :  ")                                                                                                 
    import codeforhandcricket
    codeforhandcricket.menu()