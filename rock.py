import random
while True:
    uscore=0
    cscore=0
    uaction=input("enter your choice\n1.Rock \n2.paper \n3.Scissor:")
    pactions=["rock","paper","scissor"]
    caction=random.choice(pactions)
    print(f"\nYour choice:{uaction} \nComputer Choice:{caction}\n")
    if uaction==caction:
        print("It's tie")
    elif((uaction=="rock" and caction=="scissor")or(uaction=="paper" and caction=="rock")or(uaction=="scissor" and caction=="paper")):
        print("You Win")
        uscore=uscore+1
    else:
        print("You lose")
        cscore=cscore+1
    print(f"\nyour Score:{uscore}\ncomputer score:{cscore}")
    play_again=input("Do you want to play again?(yes/no):")
    if play_again.lower()!="yes":
        break;
