# Rock Paper Scissors Game

## Overview
**Rock Paper Scissors** is a classic hand game brought to life in Python! Play multiple rounds against a computer bot and see who can win the most rounds. This interactive game lets you choose how many rounds you want to play and tracks scores throughout the match.

## Project Structure
```
Rock Paper Scissors/
├── main.py      # Main game file
└── README.md    # This file
```


## How to Run
```bash
python main.py
```


## Python Basics Used in This Project

### 1. **Function Definition with Parameters**
```python
def game(counter):
```
- Defines a function that accepts one parameter `counter`
- `counter` stores the number of rounds to play
- Encapsulates game logic in reusable code
- **Concept**: Functions, parameters, and code organization


### 2. **Lists**
```python
x = ["rock", "paper", "scissors"]
```
- Creates a list of three string choices
- Lists store multiple items in order
- Lists are mutable (can be modified)
- Indexed from 0: x[0]="rock", x[1]="paper", x[2]="scissors"
- **Concept**: Lists, collections, and indexing

### 3. **While Loop with Counter**
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

### 4. **Nested If/Elif/Else Statements**
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


### 5. **Conditional Logic - Game Outcome**
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

### 6. **Multiple Elif Blocks**
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

### 7. **Loop Counter Decrement**
```python
counter -= 1
```
- Decrements counter by 1 each round
- Eventually makes `counter == 0`, ending loop
- Controls loop iterations
- **Concept**: Loop control and iteration counting

### 8. **Type Conversion**
```python
counter = int(input(...))
```
- `input()` returns a string
- `int()` converts string to integer
- Necessary because input is always a string
- Example: "3" (string) → 3 (integer)
- **Concept**: Type casting and data conversion

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


## Fun Facts
- Rock Paper Scissors is played competitively worldwide
- There are tournaments with prize money!
- The game has a mathematical balance (each move beats one, loses to one, ties with one)
- Computer AI can learn patterns if you play multiple games
- This simple game teaches fundamental programming concepts

