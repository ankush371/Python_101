# Guess the Number Game - Man vs Machine

## Overview
**Guess the Number** is an interactive turn-based game where you compete against an AI bot to guess a randomly selected number between 1 and 100. The game features strategic turns where the human player and the bot take turns making guesses. You have 10 attempts to guess the number before the bot outsmarts you!

## Project Structure
```
Guess_the_Number/
├── main.py      # Main game file
└── README.md    # This file
```


## How to Run
```bash
python main.py
```

## Python Basics Used in This Project


### 1. **While Loop with Counter**
```python
counter = 0
while counter < 10:
    counter += 1
    # Game logic here
```
- Repeats game turns up to 10 times
- Counter tracks number of attempts
- Loop continues until condition becomes False
- **Concept**: Iteration and loop control

### 2. **Compound Assignment Operator**
```python
counter += 1
```
- Shorthand for `counter = counter + 1`
- Increments counter by 1
- **Concept**: Assignment operators and operators (+=)

### 3. **Input Function and Type Conversion**
```python
guess = int(input('Enter your guess: '))
```
- `input()`: Collects user input as a string
- `int()`: Converts the string to an integer
- **Concept**: User input, type conversion, and type casting

### 4. **Comparison Operators**
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

### 5. **If/Elif/Else Statements**
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

### 6. **Try/Except Block (Exception Handling)**
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

### 7. **Break Statement**
```python
else:
    print(f' Congratulations! YOU guessed the number {number} correctly!')
    break  # The human wins, end the game!
```
- Exits the loop immediately
- Ends the game when someone guesses correctly
- **Concept**: Loop control and early exit

### 8. **Time Module - sleep() Function**
```python
time.sleep(1.5)  # Adding a delay for better readability
```
- Pauses program execution for 1.5 seconds
- Creates dramatic effect and improves user experience
- **Concept**: Program timing and delays


### 9. **While/Else Construct**
```python
while counter < 10:
    # loop code
    break  # exits loop
else:
    # This executes only if loop completes without break
    print(f'\nGame Over! 10 attempts reached. The number was {number}.')
```
- `else` block executes only if while loop completes normally (without break)
- Handles the case where no one guesses the number in 10 turns
- **Concept**: Advanced loop control and edge case handling


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
| Loops | `while counter < 10:` | Repeat code |
| Loop Control | `break` | Exit loop early |
| Exception Handling | `try/except` | Handle errors gracefully |
| String Formatting | F-strings | Embed variables in text |
| Time Delays | `time.sleep()` | Control execution timing |
| Operators | `+=`, `//` | Shorthand operations |
| While/Else | Loop + else block | Handle normal completion |
| Main Block | `if __name__ == '__main__':` | Script entry point |

---


## Requirements
- Python 3.6 or higher (for f-string support)
- No external libraries required (uses only Python standard library)




## Fun Facts
- The bot's binary search algorithm can find any number 1-100 in at most **7 guesses**
- You get **10 attempts**, which is actually more than what the bot theoretically needs
- Invalid input costs you a turn, so careful typing matters!
- The `time.sleep()` creates suspense as the "bot thinks".

