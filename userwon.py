##single player
import random
import math
global comp_run
global user_run
global s
global i

##when comp is bowling
def comp_bowl(target):
    i=0
    s=0
    comp_run=0
    user_run=0
    target=target+1
    print("The target for the Robo to win is"+str(target)+"runs")
    while i<=balls:
        comp_run = random.randint(1,10)
        user_run = int(input("Enter your run: "))
        
        if user_run>0 and user_run<=10:
            print("Robo's runs :"+str(comp_run))
            if user_run != comp_run:
                s = s + user_run
                print("Total score :"+str(s))
                global left_runs
                left_runs = target-s
                if left_runs >0:
                    print("Runs left to win :"+str(left_runs)+" runs")
                    i=i+1
                    left = balls - i
                    print("You have "+str(left)+"balls left")

                    if left==0:
                        print("You Won")
                        break
                    else:
                        continue
                elif left_runs==0 or left_runs<0:
                    print("You won")
                    break
            else:
                print("You are out")
                break
        else:
            print("Please enter the number between 1-10")



##When user chooses to bowl
def user_bowl():
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
                s = s + comp_run
                print("Total score: " + str(s))
                i=i+1
                left = balls - i
                print("You have " + str(left) + " balls left")
                
                if left ==0:
                    print("The total score of robo is: " + str(s) + "runs")
                    break
                else:
                    continue
            
            else:
                s = s+1
                print("Robo gets out")
                print("Target for the user is " + str(s) + " runs")
                break
        else:
            print("Please enter runs between 1-10")

    comp_bowl(s)



##Function for comp_bat
def comp_bat(target):
    i=0
    s=0
    comp_run=0
    user_run=0
    target=target+1
    
    
    print("Now the Robo need to bat.\nThe target score for the Robo is " + str(target) + "runs")
    
    while i<=balls:
        comp_run = random.randint(1,10)
        user_run = int(input("Enter your run: "))
            
        if user_run>0 and user_run<=10:
                print("Robo's runs: " + str(comp_run))
                if user_run != comp_run:
                    s = s + comp_run
                    print("Total score: " + str(s))
                    global left_runs
                    left_runs = target - s
                    if left_runs >0:
                        print("Runs left to win: " + str(left_runs) + " runs")
                        i=i+1
                        left = balls - i
                        print("You have " + str(left) + " balls left")
                        if left ==0:
                            print("Robo missed your target.\nRobo loses.")
                            break
                        else:
                            continue
                      
                            
                        
                    elif left_runs == 0 or left_runs < 0:
                        print("Robo won")
                        break
            
                else:
                    print("Robo gets out")
                    ##print("User loses the game by " + str(left_runs) + " runs")
                    break
        else:
            print("Plesase enter runs between 1-10")



##when user chooses to bat
def user_bat():
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
                print("User gets out")
                print("Target for the Robo is " + str(s) + " runs")
                break
        else:
            print("Please enter runs between 1-10")
    
    comp_bat(s)



##When User wins the toss
def user_win_toss():
    
    print("choose batting or bowling")
    choose = input()
    print("User has choose for  " + str(choose))
    if choose == "Batting" or choose == "batting":
        user_bat()
    else:
        user_bowl()



##User wins the toss
##Common area
over = int(input("Enter the number of overs you want to play for[1-3]: "))

balls = over *6
if over==1 :
    print("You have choose to play for " + str(over) + " over" + " and " + str(balls) + " balls") 
else :
    print("You have choose to play for " + str(over) + " overs"  + " and " + str(balls) + " balls")

##user_win_toss()
