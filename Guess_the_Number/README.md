# Guess the Number Game - Man vs Machine

## Overview
**Guess the Number** is an interactive turn-based game where you compete against an AI bot to guess a randomly selected number between 1 and 100. The game features strategic turns where the human player and the bot take turns making guesses. You have 15 attempts to guess the number before the bot outsmarts you!

## Features
- **Man vs Machine Gameplay**: Interactive competition between player and AI bot
- **Smart Bot AI**: Uses binary search algorithm for optimal guessing strategy
- **Turn-based System**: Alternating turns between human and bot players
- **Attempt Limit**: 15 turns maximum to guess the number
- **User Feedback**: Clear feedback on each guess (too high, too low, or correct)
- **Error Handling**: Validates user input and handles invalid entries
- **Dramatic Pauses**: Time delays for better game experience and tension building

## How to Run
```bash
python main.py
```

The game will:
1. Welcome you and explain the rules
2. Randomly select a secret number between 1 and 100
3. Alternate turns between you and the bot
4. Provide feedback on each guess
5. Determine the winner when someone guesses correctly or attempts run out

## Example Gameplay
```
Welcome to the Guess the Number Game: Man vs Machine!
I have selected a number between 1 and 100.
You have 15 attempts to guess the number before the bot does!

----------------------------------- Turn 1 -----------------------------------
Enter your guess: 50
Too high! Try a lower number.

Bot is thinking...
Bot guesses: 75
Bot guess is too high.

----------------------------------- Turn 2 -----------------------------------
Enter your guess: 25
Too low! Try a higher number
...
Congratulations! YOU guessed the number 42 correctly!
```

---

## Python Basics Used in This Project

### 1. **Import Statements**
```python
import random
import time
```
- `random`: Provides randomization functions for game logic
- `time`: Allows program to pause execution for dramatic effect
- **Concept**: Importing external modules from Python standard library

### 2. **Function Definition**
```python
def guess_the_number():
```
- Encapsulates the entire game logic in a reusable function
- Makes code organized and maintainable
- **Concept**: Function definition and code organization

### 3. **Random Module - randint() Function**
```python
number = random.randint(1, 100)
```
- Generates a random integer between 1 and 100 (inclusive)
- Creates the secret number for the game
- **Concept**: Randomization and random number generation

### 4. **Variables and Assignment**
```python
number = random.randint(1, 100)
bot_low = 1
bot_high = 100
counter = 0
```
- Store game state and player information
- Initialize values for tracking game progress
- **Concept**: Variables, initialization, and data types (integers)

### 5. **Print Function with Parameters**
```python
print(f'\n----------------------------------- Turn {counter} -----------------------------------')
print("Bot is thinking...", end="")
```
- `end=""` parameter prevents automatic newline after print
- Allows continuation of output on the same line
- **Concept**: Print function parameters and text formatting

### 6. **F-Strings (Formatted String Literals)**
```python
print(f'\n----------------------------------- Turn {counter} -----------------------------------')
print(f' Congratulations! YOU guessed the number {number} correctly!')
```
- Embeds variables directly into strings
- Uses `{variable}` syntax for substitution
- **Concept**: String formatting and template interpolation

### 7. **While Loop with Counter**
```python
counter = 0
while counter < 15:
    counter += 1
    # Game logic here
```
- Repeats game turns up to 15 times
- Counter tracks number of attempts
- Loop continues until condition becomes False
- **Concept**: Iteration and loop control

### 8. **Compound Assignment Operator**
```python
counter += 1
```
- Shorthand for `counter = counter + 1`
- Increments counter by 1
- **Concept**: Assignment operators and operators (+=)

### 9. **Input Function and Type Conversion**
```python
guess = int(input('Enter your guess: '))
```
- `input()`: Collects user input as a string
- `int()`: Converts the string to an integer
- **Concept**: User input, type conversion, and type casting

### 10. **Comparison Operators**
```python
if guess < number:
    print('Too low! Try a higher number')
elif guess > number:
    print('Too high! Try a lower number.')
else:
    print(f' Congratulations! YOU guessed the number {number} correctly!')
```
- `<` (less than): Check if guess is too low
- `>` (greater than): Check if guess is too high
- `==` (equal to): Check if guess is correct
- **Concept**: Comparison operators and conditional logic

### 11. **If/Elif/Else Statements**
```python
if guess < number:
    # action 1
elif guess > number:
    # action 2
else:
    # action 3
```
- Controls program flow based on conditions
- Only one block executes at a time
- **Concept**: Conditional statements and branching logic

### 12. **Try/Except Block (Exception Handling)**
```python
try:
    guess = int(input('Enter your guess: '))
    # validation logic
except ValueError:
    print('Invalid input. Please enter a valid integer (You wasted a turn!).')
```
- `try`: Attempts to execute code that might cause an error
- `except ValueError`: Catches conversion errors (non-integer input)
- Prevents program crash from invalid user input
- **Concept**: Error handling and exception management

### 13. **Break Statement**
```python
else:
    print(f' Congratulations! YOU guessed the number {number} correctly!')
    break  # The human wins, end the game!
```
- Exits the loop immediately
- Ends the game when someone guesses correctly
- **Concept**: Loop control and early exit

### 14. **Time Module - sleep() Function**
```python
time.sleep(1.5)  # Adding a delay for better readability
```
- Pauses program execution for 1.5 seconds
- Creates dramatic effect and improves user experience
- **Concept**: Program timing and delays

### 15. **Integer Division Operator**
```python
bot_guess = (bot_low + bot_high) // 2
```
- `//` performs division and rounds down to nearest integer
- Calculates midpoint for binary search algorithm
- Example: `7 // 2 = 3` (not 3.5)
- **Concept**: Arithmetic operators and binary search strategy

### 16. **Variable Update for Bot Strategy**
```python
if bot_guess < number:
    bot_low = bot_guess + 1       
elif bot_guess > number:
    bot_high = bot_guess - 1
```
- Updates search boundaries based on feedback
- Implements binary search algorithm (halves search space each turn)
- **Concept**: Algorithm design and state management

### 17. **While/Else Construct**
```python
while counter < 15:
    # loop code
    break  # exits loop
else:
    # This executes only if loop completes without break
    print(f'\nGame Over! 15 attempts reached. The number was {number}.')
```
- `else` block executes only if while loop completes normally (without break)
- Handles the case where no one guesses the number in 15 turns
- **Concept**: Advanced loop control and edge case handling

### 18. **Comments**
```python
# ---------------------------------------------------------------------------------
#               HUMAN TURN
# =================================================================================
```
- Document code sections and explain logic
- Improve code readability and maintainability
- **Concept**: Code documentation and best practices

### 19. **Main Block / Guard Clause**
```python
if __name__ == '__main__':
    guess_the_number()
```
- Runs function only when script is executed directly
- Prevents execution if script is imported elsewhere
- Best practice for Python scripts
- **Concept**: Script execution control and modularity

---

## Binary Search Algorithm Explanation

The bot uses a **binary search** strategy to guess efficiently:

1. **Starts** with search range 1-100
2. **Guesses** the middle value: `(1 + 100) // 2 = 50`
3. **Narrows** range based on feedback:
   - If guess too low: search upper half (51-100)
   - If guess too high: search lower half (1-49)
4. **Repeats** with new midpoint until correct

**Example**: Finding 23 in 1-100
- Turn 1: Guess 50 → Too high → Range: 1-49
- Turn 2: Guess 25 → Too high → Range: 1-24
- Turn 3: Guess 12 → Too low → Range: 13-24
- Turn 4: Guess 18 → Too low → Range: 19-24
- Turn 5: Guess 21 → Too low → Range: 22-24
- Turn 6: Guess 23 → Correct! (Bot wins in 6 turns)

This algorithm guarantees finding any number in at most ~7 guesses (log₂ 100 ≈ 6.64).

---

## Python Concepts Summary Table

| Concept | Example | Purpose |
|---------|---------|---------|
| Imports | `import random, time` | Access external modules |
| Functions | `def guess_the_number():` | Organize code |
| Random Numbers | `random.randint(1, 100)` | Generate secret number |
| Input/Output | `input()`, `print()` | User interaction |
| Type Conversion | `int(input())` | Convert string to integer |
| Comparison | `<`, `>`, `==` | Compare values |
| Conditionals | `if/elif/else` | Decision making |
| Loops | `while counter < 15:` | Repeat code |
| Loop Control | `break` | Exit loop early |
| Exception Handling | `try/except` | Handle errors gracefully |
| String Formatting | F-strings | Embed variables in text |
| Time Delays | `time.sleep()` | Control execution timing |
| Operators | `+=`, `//` | Shorthand operations |
| While/Else | Loop + else block | Handle normal completion |
| Main Block | `if __name__ == '__main__':` | Script entry point |

---

## Game Rules
1. A random number between 1-100 is selected
2. Players alternate turns (you first, then bot)
3. Maximum 15 turns total (including both players)
4. First to guess correctly wins
5. Invalid input costs you a turn
6. Game ends immediately when someone wins
7. If 15 turns pass without a winner, it's a draw

## Requirements
- Python 3.6 or higher (for f-string support)
- No external libraries required (uses only Python standard library)

## Project Structure
```
Guess_the_Number/
├── main.py      # Main game file
└── README.md    # This file
```

## Difficulty Analysis
- **Difficulty for Human**: Medium (random guessing vs. strategic bot)
- **Bot Strategy**: Optimal (binary search always wins in ~7 attempts)
- **Player Advantage**: 15 attempts vs. bot's limited optimal turns

## Learning Outcomes
This project teaches:
- Game logic and turn-based systems
- Control flow (if/elif/else, while loops)
- Error handling with try/except
- Algorithm implementation (binary search)
- User interaction and input validation
- State management in games
- Python best practices

## Fun Facts
- The bot's binary search algorithm can find any number 1-100 in at most **7 guesses**
- You get **15 attempts**, which is actually double what the bot theoretically needs
- Invalid input costs you a turn, so careful typing matters!
- The `time.sleep()` creates suspense as the "bot thinks"

## Future Enhancements
- Add difficulty levels (smaller/larger ranges)
- Track statistics (wins, losses, average guesses)
- Add a scoreboard for multiple rounds
- Implement different AI strategies
- Create a GUI version with graphics
- Add sound effects and music
- Multiplayer mode (two humans competing)

