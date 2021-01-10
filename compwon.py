##single player
import random
import math
global comp_run
global user_run
global s
global i

##When user is bowling
def user_bowl(target):
    i=0
    s=0
    comp_run=0
    user_run=0
    target=target+1
    print("The target for The Robo to win is " + str(target) + " runs")
    while i <=balls:
        comp_run = random.randint(1,10)
        user_run = int(input("Enter your run: "))
        if user_run>0 and user_run<=10:
            print("Robo's runs: " + str(comp_run))
            if user_run != comp_run:
                s = s + comp_run
                print("Total score: " + str(s))
                global left_runs
                left_runs = target-s
                if left_runs >0:
                    print("Runs left to win: " + str(left_runs) + " runs")
                    i=i+1
                    left = balls - i
                    print("You have " + str(left) + " balls left")
                
                    if left ==0:
                        print("Robo lost it")
                        break
                    else:
                        continue
                elif left_runs == 0 or left_runs < 0:
                    print("Robo won")
                    break
            else:
                print("Robo gets out")
                print("You won")
               ## print("target for the user is " + str(s) + " runs")
                break
        else:
            print("Plesase enter runs between 1-10")
    



##When computer chooses to bowl
def comp_bowl():
    i=0
    s=0
    comp_run=0
    user_run=0
    target=0
    while i<=balls:
        comp_run = random.randint(1,10)
        user_run = int(input("Enter your run: "))
        if user_run>0 and user_run<=10:
            print("Robo's runs: " + str(comp_run))
            if user_run != comp_run:
                s = s + user_run
                print("Total score: " + str(s))
                i=i+1
                left = balls - i
                print("You have " + str(left) + " balls left")
                
                if left ==0:
                    print("The total score of user is: " + str(s) + "runs")
                    break
                else:
                    continue
            
            else:
                s = s+1
                print("User gets out")
                print("Target for The Robo is " + str(s) + " runs")
                break
        else:
            print("Please enter runs between 1-10")

    user_bowl(s)
    

##Function for user_bat
def user_bat(target):
    i=0
    s=0
    comp_run=0
    user_run=0
    target=target+1
    
    
    print("Now the user need to bat.\nThe target score for user is " + str(target) + "runs")
    
    while i<=balls:
        comp_run = random.randint(1,10)
        user_run = int(input("Enter your run: "))
            
        if user_run>0 and user_run<=10:
                print("Robo's runs: " + str(comp_run))
                if user_run != comp_run:
                    s = s + user_run
                    print("Total score: " + str(s))
                    global left_runs
                    left_runs = target - s
                    if left_runs >0:
                        print("Runs left to win: " + str(left_runs) + " runs")
                        i=i+1
                        left = balls - i
                        print("You have " + str(left) + " balls left")
                        if left ==0:
                            print("You missed your target.\nYou lost it.")
                            break
                        else:
                            continue
                      
                            
                        
                    elif left_runs == 0 or left_runs < 0:
                        print("You won")
                        break
            
                else:
                    print("User gets out")
                    ##print("User loses the game by " + str(left_runs) + " runs")
                    break
        else:
            print("Plesase enter runs between 1-10")
        

##When computer chooses to bat
def comp_bat():
    i=0
    s=0
    comp_run=0
    user_run=0
    target=0
    while i <=balls:
        comp_run = random.randint(1,10)
        user_run = int(input("Enter your run: "))
        if user_run>0 and user_run<=10:
            print("Robo's runs: " + str(comp_run))
            if user_run != comp_run:
                s = s + comp_run
                print("Total score: " + str(s))
                i=i+1
                left = balls - i
                print("You have " + str(left) + " balls left")
                
                if left ==0:
                    print("The total score of robot is: " + str(s) + "runs")
                    break
                else:
                    continue
            else:
                print("Robo gets out")
                print("Target for the user is " + str(s) + " runs")
                break
        else:
            print("Plesase enter runs between 1-10")
    
    user_bat(s)

##When computer wins the toss
def comp_win_toss():
    
    choose = ['Batting','Bowling']
    comp_choice = random.choice(choose)
    print("Computer have choose to " + str(comp_choice))
    if comp_choice == "Batting":
        comp_bat()
    else:
        comp_bowl()


##Computer wins the toss
##Common area
over = int(input("Enter the number of overs you want to play for[1-3]: "))

balls = over *6
print("You have choose to play for " + str(over) + " over" + " and " + str(balls) + " balls") if over==1 else print("You have choose to play for " + str(over) + " overs"  + " and " + str(balls) + " balls")
##comp_win_toss()







    
