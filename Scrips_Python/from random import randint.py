from random import randint
import os

status_menu = True

def main_menu():
    global status_opts
    status_opts= True

    
    print (":::: main menu :::::")
    print ("[1]. start game ")
    print ("[2]. help")
    print ("[3]. exit ")
    while status_opts:
        opt = int(input("press any option:"))
        if opt <1 or opt > 3 :
            print ("error. press any option between 1 and 3 ")
        else:
            status_opts = False
    return opt
    
    opt = int (input("press any option: "))
    exit

while status_menu:
   os.system('clear')
   op= main_menu()
   if op ==1:
     os.system('clear')
     print ("welcome to number race ")
     
     players= int (input ("press number of players [1:4]"))
     print ("::::.level menu:::")
     print ("[1]. basic")
     print ("[2]. intermediate")
     print ("[3]. advance")
     print ("[4]. expert")
     opt = int(input("press any option: "))
     if opt ==1:
         pos=20
     elif opt ==2:
         pos =30
     elif opt ==3:
         pos = 50
     else:
         pos= 100
     #star game 
     status_game = True
     
     roll_count = 0
     roll_acum = 0
     
     while status_game:
         key = input ("press any key to roll dice...")
         dice1 = randint(1,6)
         dice2 = randint(1,6)
         
         print (f"dice 1: {dice1}")
         print (f"dice 2: {dice2}")
         total = dice1 + dice2
         print (f"total roll: {total}")

         
         roll_count +=1  # roll_count = roul_count + 1
         roll_acum += total
         print (f"total game: {roll_acum}")

         
         if roll_acum >= pos:
             print (":::: you win, congratulations ::::")
             status_game = False
             
     print ("statitics")
     print (f"total roll:{roll_count}")
     print (f"total dices:{roll_acum}")

     
     
     
     key = ("press any key to go to the main menu..")
   elif op ==2:
     print ("Game under construction")
     key = ("press any key to go to the main menu..")
   else: 
     print ("see 'u later")
     key = ("press any key to exit..")
     break



    
    