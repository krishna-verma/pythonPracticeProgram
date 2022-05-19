from ctypes.wintypes import POINT
import random
round = int(input("HOW MANY ROUNDS DO YOU WANT TO PLAY : "))
point=0

for i in range(round):
    print("\n\n*****************ROUND",i+1,"*******************\n\n")
    sys = random.randint(1, 3)
    print("""
          Rock    :  1
          Paper   :  2
          Scissor :  3
          """)
    user = int(input("enter your choise : "))
    print()

    if(sys == 1):
        print("player1 = Rock")
    elif(sys == 2):
        print("player1 = Paper")
    elif(sys == 3):
        print("player1 = Scissor")

    print()

    if(user == 1):
        print("YOU = Rock")
    elif(user == 2):
        print("YOU = Paper")
    elif(user == 3):
        print("YOU = Scissor")
    else:
        print("invalid choise")

    print()
    print()

    if(user == 3 and sys == 1):
        print("***************YOU LOSE**************")

    elif(sys > user):
        print("***************YOU LOSE**************")

    elif(sys == user):
        print("***************DRAW**************")

    elif(sys < user and (user == 1 or 2 or 3)):
        print("***************YOU WIN**************")
        point=point+1
    
print("\n\n******************YOUR SCORE = ",point,"*********************\n\n")
    
