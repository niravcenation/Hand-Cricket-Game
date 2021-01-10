import random
import math
import csv
import sys

def main():
    toss_duo()

def toss_duo():
    print("Welcome for the toss")
    print
    time_to_toss=input("""
                                Select 
                                1. Even
                                2. Odd
                                            """)     
    player_input = int(input("Enter your number[1-10]="))
    opp_input = int(input("Player2,enter your number[1-10]="))
    
    print("TOSS: You: " + str(player_input))
    print("TOSS: Player_2: " + str(opp_input))
    
    toss_sum=player_input+opp_input
    print(toss_sum)

    if toss_sum % 2 != 0:
        abc = "2"
    else:
        abc = "1"

    if time_to_toss != abc:
        print("You lost the toss\nPlayer_2 won the toss")
    else :
        print("You won the toss\nPlayer_2 lost the toss")
