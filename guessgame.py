from random import randint

actual_num = randint(1,10)

while True:

    guess_num = int(input("Guess a number between 1 and 10: "))
    
    if guess_num == actual_num:
        print("you gussed it right")
        case = input("Want to play again? (y/n): ")
        if case=="y":
            actual_num = randint(1,10)
        else:
            print("Thank you for playing...")
            break
    
    elif guess_num > actual_num:
        print("Too high")
    else:
        print("Too low")





    
