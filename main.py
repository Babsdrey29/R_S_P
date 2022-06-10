import random


print ("The Rock Paper Scissors Challenge")
print("The winner is determined according to a set of rules, the rules are as follows:\n rock vs scissors; rock wins\n paper vs rock; paper wins\n scissors vs paper; scissors wins ")
#highlighting user choice
possible_options = ["rock", "paper", "scissors"]
print("\nselect choice from:")
print("R")
print("S")
print("P")
while True:
    letter = ['R','P','S']
    choice = input("enter choice for user:")
    if choice in letter:
        if choice == ('R'):
            user_option = "rock"
        elif choice == ('P'):
            user_option = "paper"
        else:
            user_option = "scissors"

        print("user picked " + user_option)
        print("\nNow its computer turn to pick")
        computer_option = random.choice(possible_options)
        while computer_option == choice:
            computer_option = random.choice(possible_options)
            if computer_option == (possible_options[0]):
                computer_option = "rock"
            elif computer_option == (possible_options[1]):
                computer_option = "paper"
            else:
                computer_option = "scissors"
        print("computer picked " + computer_option)
        print("Player; " + user_option + ":" + "computer; " computer_option)

        if user_option == computer_option:
                print("It's a tie!")
        elif user_option == "paper":
            if computer_option == "rock":
                print("user wins!")
            else:
                print("computer wins!")
        elif user_option == "scissors":
            if computer_option == "paper":
                print("user wins!")
            else:
                print("computer wins.")
        elif user_option == "rock":
            if computer_option == "scissors":
                print("user wins!")
            else:
                print("computer wins")
        next_game = input("Would you like to play again? (yes/no): ")
        if next_game == "yes" or  next_game == "YES" or next_game == "Yes" or next_game == "y":
            continue

    
        break
    else:
        print ('PLease try again, enter R,S or P')
    
        next_game = input("Would you like to try again? (yes/no): ")
        if next_game == "no":
            break
