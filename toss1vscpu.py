import random
import math
import csv
import sys

def main():
    toss()
    
def toss():
    print("Welcome for the toss")
    time_to_toss=input("""
                                Select 
                                1. Even
                                2. Odd
                                            """)
    playerinput = int(input("Enter your number[1-10]="))
    cpuinput = math.ceil(random.random()*10)   
    print("TOSS:You "+str(playerinput))
    print("TOSS:Comp: " + str(cpuinput))

    toss_sum=playerinput+cpuinput
    print(toss_sum)
    

    if toss_sum % 2 != 0:
        abc = "2"
    else:
        abc = "1"

    
    if time_to_toss != abc:
        print("You lost the toss\nRobo won the toss")
        import compwon
        compwon.comp_win_toss()
    else :
        print("You won the toss\nRobo lost the toss")
        import userwon
        userwon.user_win_toss()


