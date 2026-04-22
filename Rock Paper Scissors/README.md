# Rock Paper Scissors Game

## Overview
**Rock Paper Scissors** is a classic hand game brought to life in Python! Play multiple rounds against a computer bot and see who can win the most rounds. This interactive game lets you choose how many rounds you want to play and tracks scores throughout the match.

## Features
- **Customizable Rounds**: Choose how many rounds you want to play
- **Score Tracking**: Keeps track of your score and the bot's score
- **Random Bot Choices**: Bot makes random selections to keep gameplay unpredictable
- **Case-Insensitive Input**: Accepts uppercase or lowercase inputs
- **Game Results**: Announces winner after all rounds complete
- **Best of Format**: Tracks wins across multiple rounds (Best of 3, 5, etc.)

## How to Run
```bash
python main.py
```

The game will:
1. Ask how many rounds you want to play
2. For each round, you enter your choice (rock, paper, or scissors)
3. Bot randomly selects its choice
4. Results are displayed with updated scores
5. Final winner is announced after all rounds

## Example Gameplay
```
How many rounds do you want to play? (Best of 3) : 3
Best of 3 rounds
Enter your choice (rock, paper, scissors): rock
You win! Bot chose scissors.
Your score: 1
Bot score: 0
Best of 2 rounds
Enter your choice (rock, paper, scissors): paper
You lose! Bot chose scissors.
Your score: 1
Bot score: 1
Best of 1 rounds
Enter your choice (rock, paper, scissors): scissors
You win! Bot chose rock.
Your score: 2
Bot score: 1
Congratulations! You won the game!
```

## Game Rules
- **Rock beats Scissors**: Rock crushes scissors
- **Scissors beats Paper**: Scissors cuts paper
- **Paper beats Rock**: Paper covers rock
- **Tie**: If both choose the same, it's a tie (no points awarded)
- **Winner**: First to win the most rounds wins the game

---

## Python Basics Used in This Project

### 1. **Function Definition with Parameters**
```python
def game(counter):
```
- Defines a function that accepts one parameter `counter`
- `counter` stores the number of rounds to play
- Encapsulates game logic in reusable code
- **Concept**: Functions, parameters, and code organization

### 2. **Import Statements Inside Functions**
```python
def game(counter):
    import random
```
- Imports `random` module inside the function
- Module is only loaded when function is called
- Typically imports are placed at top of file (best practice)
- **Concept**: Module importing and scope

### 3. **Variable Assignment and Initialization**
```python
score_user = 0
score_bot = 0
```
- Initialize score variables to 0
- Tracks points for both players
- Mutable data (can be changed)
- **Concept**: Variables, initialization, and integer data type

### 4. **Lists**
```python
x = ["rock", "paper", "scissors"]
```
- Creates a list of three string choices
- Lists store multiple items in order
- Lists are mutable (can be modified)
- Indexed from 0: x[0]="rock", x[1]="paper", x[2]="scissors"
- **Concept**: Lists, collections, and indexing

### 5. **While Loop with Counter**
```python
while counter != 0:
    # game logic
    counter -= 1
```
- Repeats the game loop for specified number of rounds
- `!=` means "not equal to"
- Loop continues while counter is not zero
- Counter decrements each iteration
- **Concept**: Loops, iteration, and loop control

### 6. **Comparison Operator (!= )**
```python
while counter != 0:
```
- `!=` checks if values are NOT equal
- Returns True if counter is not 0, False otherwise
- **Concept**: Comparison operators and boolean logic

### 7. **Random Module - choice() Function**
```python
bot_choice = random.choice(x)
```
- Randomly selects one item from the list
- Each choice (rock, paper, scissors) has equal probability
- Different choice each round (usually)
- **Concept**: Randomization and probability

### 8. **F-String Formatting**
```python
print(f"Best of {counter} rounds")
```
- Embeds the `counter` variable in the string
- Shows remaining rounds to play
- Makes output dynamic and informative
- **Concept**: String formatting and template interpolation

### 9. **Input Function and String Methods**
```python
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
```
- `input()`: Collects user input as a string
- `.lower()`: Converts string to lowercase
- Allows user to input "ROCK", "Rock", or "rock" (all work)
- Chaining methods (method on method)
- **Concept**: Input, string methods, and method chaining

### 10. **Nested If/Elif/Else Statements**
```python
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
    # more conditions
```
- Multiple levels of conditions
- Inner `if/else` nested inside `elif` block
- Checks all possibilities for outcome determination
- **Concept**: Nested conditionals and complex logic flow

### 11. **Comparison Operator (==)**
```python
if user_choice == bot_choice:
```
- `==` checks if two values are equal
- Returns True if equal, False otherwise
- String comparison (case-sensitive, but we used `.lower()`)
- **Concept**: Equality operator and boolean logic

### 12. **Compound Assignment Operators**
```python
score_user += 1
score_bot += 1
counter -= 1
```
- `+=` means `score_user = score_user + 1`
- `-=` means `counter = counter - 1`
- Shorthand for increment/decrement operations
- **Concept**: Assignment operators and shorthand notation

### 13. **Print Function with Multiple Arguments**
```python
print("It's a tie! Bot also chose", bot_choice)
```
- Multiple arguments separated by commas
- Prints with spaces between arguments
- Combines strings and variables
- **Concept**: Print function and string concatenation

### 14. **String Concatenation via Print**
```python
print("You win! Bot chose", bot_choice)
```
- Print automatically joins arguments with spaces
- Alternative to f-strings for combining strings
- **Concept**: String joining and output formatting

### 15. **Conditional Logic - Game Outcome**
```python
if user_choice == "rock":
    if bot_choice == "scissors":
        print("You win! Bot chose scissors.")
        score_user += 1
    else:  # bot_choice must be "paper"
        print("You lose! Bot chose paper.")
        score_bot += 1
```
- Implements game rules: rock beats scissors, paper beats rock
- Shows all possible outcomes for each choice
- **Concept**: Game logic and algorithm design

### 16. **Multiple Elif Blocks**
```python
elif user_choice == "paper":
    if bot_choice == "rock":
        # you win
    else:
        # you lose
elif user_choice == "scissors":
    if bot_choice == "paper":
        # you win
    else:
        # you lose
```
- Handles all three possible user choices
- Each branch has its own logic
- First matching condition executes
- **Concept**: Multi-way branching and decision trees

### 17. **Loop Counter Decrement**
```python
counter -= 1
```
- Decrements counter by 1 each round
- Eventually makes `counter == 0`, ending loop
- Controls loop iterations
- **Concept**: Loop control and iteration counting

### 18. **Final Score Comparison**
```python
if score_user > score_bot:
    print("Congratulations! You won the game!")
elif score_user < score_bot:
    print("Sorry! You lost the game!")
else:
    print("It's a tie game!")
```
- Compares final scores after all rounds
- Uses `>` (greater than) and `<` (less than)
- `else` catches tie scenario
- Announces overall winner
- **Concept**: Comparison operators and final results

### 19. **Main Block Guard Clause**
```python
if __name__ == "__main__":
    counter = int(input("How many rounds do you want to play? (Best of 3) : "))
    game(counter)
```
- Code only runs when script is executed directly
- Not executed if imported as module
- Gets number of rounds from user via `input()`
- `int()` converts string input to integer
- Calls the game function with the counter value
- **Concept**: Script entry point and type conversion

### 20. **Type Conversion**
```python
counter = int(input(...))
```
- `input()` returns a string
- `int()` converts string to integer
- Necessary because input is always a string
- Example: "3" (string) → 3 (integer)
- **Concept**: Type casting and data conversion

---

## Game Logic Flowchart

```
1. Get number of rounds from user
2. Initialize scores (user=0, bot=0)
3. For each round:
   a. Bot randomly chooses rock/paper/scissors
   b. User enters their choice
   c. Compare choices:
      - Same = Tie (no points)
      - Rock vs Scissors = Rock wins
      - Scissors vs Paper = Scissors wins
      - Paper vs Rock = Paper wins
   d. Update scores
4. Compare final scores
5. Announce winner
```

---

## Python Concepts Summary Table

| Concept | Example | Purpose |
|---------|---------|---------|
| Functions | `def game(counter):` | Organize code |
| Imports | `import random` | Access modules |
| Variables | `score_user = 0` | Store data |
| Lists | `["rock", "paper", "scissors"]` | Store multiple items |
| While Loop | `while counter != 0:` | Repeat code |
| Comparison | `==`, `<`, `>`, `!=` | Compare values |
| Conditionals | `if/elif/else` | Decision making |
| String Methods | `.lower()` | Transform strings |
| Random | `random.choice()` | Random selection |
| F-Strings | `f"Best of {counter}"` | Format strings |
| Input | `input()` | Get user input |
| Type Conversion | `int(input())` | Convert types |
| Assignment Ops | `+=`, `-=` | Shorthand operations |
| Print | `print(x, y)` | Output text |
| Nested If | If inside elif | Complex logic |

---

## Requirements
- Python 3.0 or higher
- No external libraries required (uses only Python standard library)

## Project Structure
```
Rock Paper Scissors/
├── main.py      # Main game file
└── README.md    # This file
```

## Gameplay Tips
1. **No pattern**: Since the bot chooses randomly, don't try to predict it
2. **Any number**: You can play best of 1, 3, 5, 7, etc.
3. **Be careful**: Typos are forgiven (it's case-insensitive), but exact spelling matters
4. **Keep score**: Pay attention to running scores to know where you stand

## Strategy Notes
- The bot has a **50% win rate** because it chooses randomly
- Human players have a **1/3 chance** to win each round (33.3%)
- With more rounds, results tend to approach bot's advantage
- The only winning strategy is pure luck or reading the rules perfectly!

## Learning Outcomes
This project demonstrates:
- Game logic and turn-based gameplay
- Score tracking and state management
- Nested conditional logic
- Loop control and iteration
- User input handling and validation
- Random selection
- String manipulation
- Code organization with functions
- Python best practices

## Possible Improvements
- Add input validation (check for valid choices)
- Store game history
- Add difficulty levels (bot strategy)
- Implement "best of" with automatic round determination
- Add win streaks tracking
- Create leaderboard system
- Add graphical UI
- Support multiplayer mode (two humans)
- Add statistics (win percentage, games played)

## Fun Facts
- Rock Paper Scissors is played competitively worldwide
- There are tournaments with prize money!
- The game has a mathematical balance (each move beats one, loses to one, ties with one)
- Computer AI can learn patterns if you play multiple games
- This simple game teaches fundamental programming concepts

