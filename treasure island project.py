print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[shivani]
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
direction= input('You\'re at a cross road. Where do you want to go? Type "left" or "right".\n').lower()
if direction =="left":
    next_step=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if(next_step=="wait"):
        which_door = input("You arrive at the island unhamed. There ia a house with 3 doors. one red, one yellow and one blue. which colour do you have?.\n")
        if which_door=="red":
           print("Burned by fire. Game Over.")
        elif which_door=="blue":
           print("Eaten by beasts. Game Over.")
        elif which_door =="yellow":
           print("You found the tresure! You Win!")
        else:
           print("Game Over.")
    else :
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")

          
           
        
        
    
