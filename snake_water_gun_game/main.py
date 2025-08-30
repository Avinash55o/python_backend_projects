import random
"""
1 is for the snake 
-1 is for the water
0 is for the gun
"""


computer_choise= random.choice([1,-1,0]);

your_input= input("enter your choise: ")

choise_dict={'s':1, 'w': -1 ,'g': 0}
reversed_dict={1:"snake",-1:"water", 0:"gun"}

your_choise= choise_dict[your_input]

print(f"your choise is {reversed_dict[your_choise]} \n computer choise is {reversed_dict[computer_choise]}")

if computer_choise == your_choise:
    print('its a draw!')
else:
    if computer_choise == 1 and your_choise== -1:
        print("you lose!")
    elif computer_choise == 1 and your_choise== 0:
        print("you win!")
    elif computer_choise == -1 and your_choise== 1:
        print("you win!")
    elif computer_choise == -1 and your_choise== 0:
        print("you lose!")
    elif computer_choise == 0 and your_choise== -1:
        print("you win!")
    elif computer_choise == 0 and your_choise== 1:
        print("you lose!")