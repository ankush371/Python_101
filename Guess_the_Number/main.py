import random
import time

def guess_the_number():
    number = random.randint(1, 100)
    bot_low = 1
    bot_high = 100
    
    print('Welcome to the Guess the Number Game: Man vs Machine!')
    print('You have 10 attempts to guess the number before the bot does!')
    
    counter = 0
    while counter < 10:
        counter += 1
        print(f'\n----------------------------------- Turn {counter} -----------------------------------')
        
        # ---------------------------------------------------------------------------------
        #               HUMAN TURN
        # =================================================================================
        try:
            guess = int(input('Enter your guess: '))
            if guess < number:
                print('Too low! Try a higher number')
            elif guess > number:
                print('Too high! Try a lower number.')
            else:
                print(f' Congratulations! YOU guessed the number {number} correctly!')
                break  # The human wins, end the game!
        except ValueError:
            print('Invalid input. Please enter a valid integer (You wasted a turn!).')
            
        # --------------------------------------------------------------------------------
        #                BOT TURN
        # ==================================================================================
        print("\nBot is thinking...", end="")
        time.sleep(1.5)  # Adding a delay for better readability  
        
        bot_guess = (bot_low + bot_high) // 2
        print(f'\nBot guesses: {bot_guess}')
        
        if bot_guess < number:
            print('Bot guess is too low.')
            bot_low = bot_guess + 1       
        elif bot_guess > number:
            print('Bot guess is too high.')
            bot_high = bot_guess - 1
        else:
            print(f' The bot guessed the number {number} correctly! The machine wins.')
            break  # The bot wins, end the game!

    else:
        # This 'else' belongs to the 'while' loop. It triggers if the loop finishes 
        # all 10 turns without ever hitting a 'break' statement.
        print(f'\nGame Over! 10 attempts reached. The number was {number}.')

if __name__ == '__main__':
    guess_the_number()