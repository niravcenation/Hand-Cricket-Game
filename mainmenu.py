import csv
import sys

def main():
    start()

def start():
                ## menu for entering the name and mode of the playing

                name= input("Enter your name :")
                print(str(name)+"_Choose your playing mode :")


                mode=input("""
                                    1.Single Player
                                    2.Duo Player
                                                        """)
        
                if mode=="1":
                    import toss1vscpu
                    toss1vscpu.toss()
                elif mode!=1 or mode!=2:
                    print("please select valid number")
                    start()
                else :
                    import toss1vs1
                    toss1vs1.toss_duo()
                

