def game(counter):
    import random
    score_user = 0
    score_bot = 0
    x=["rock", "paper", "scissors"]
    while counter !=0:
        bot_choice = random.choice(x)
        print(f"Best of {counter} rounds")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice == bot_choice:
            print("It's a tie! Bot also chose", bot_choice)
        elif user_choice == "rock":
            if bot_choice == "scissors":
                print("You win! Bot chose scissors.")
                score_user += 1
            else:
                print("You lose! Bot chose paper.")
                score_bot += 1
        elif user_choice == "paper":
            if bot_choice == "rock":
                print("You win! Bot chose rock.")
                score_user += 1
            else:
                print("You lose! Bot chose scissors.")
                score_bot += 1
        elif user_choice == "scissors":
            if bot_choice == "paper":
                print("You win! Bot chose paper.")
                score_user += 1
            else:
                print("You lose! Bot chose rock.")
                score_bot += 1
            
        print("Your score:", score_user)
        print("Bot score:", score_bot)  
        counter -= 1
    if score_user > score_bot:
        print("Congratulations! You won the game!")
    elif score_user < score_bot:
        print("Sorry! You lost the game!")
    else:
        print("It's a tie game!")
    
if __name__ == "__main__":
    counter = int(input("How many rounds do you want to play? (Best of 3) : "))
    game(counter)