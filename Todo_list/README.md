# Todo List Application

## Overview
**Todo List** is an interactive command-line application that helps you manage your daily tasks. Add, mark tasks as complete, delete tasks, and automatically save everything to a JSON file. Your tasks persist between sessions, so you never lose your to-do list!

## Features
- **Add Tasks**: Quickly add new tasks to your to-do list
- **Mark Complete**: Check off tasks as you complete them
- **Delete Tasks**: Remove tasks you no longer need
- **Persistent Storage**: All tasks are saved to a JSON file automatically
- **Clean Interface**: Well-formatted display with task status indicators
- **User-Friendly**: Simple menu-driven interface
- **Data Validation**: Ensures task numbers and inputs are valid

## How to Run
```bash
python main.py
```

The application will:
1. Load your existing tasks from `todo.json` (or start fresh if empty)
2. Display your current to-do list
3. Show a menu with options (Add, Done, Delete, Quit)
4. Let you manage your tasks interactively
5. Automatically save changes to the JSON file

## Example Usage
```
====================================================================================================
       MY TO-DO LIST
====================================================================================================
 Nothing to do! You're all caught up.
====================================================================================================

Commands: [1] Add  [2] Done  [3] Delete  [4] Quit
Select an option: 1
Enter the new task: Buy groceries

 Added: 'Buy groceries'

====================================================================================================
       MY TO-DO LIST
====================================================================================================
 1. [ ] Buy groceries
====================================================================================================

Commands: [1] Add  [2] Done  [3] Delete  [4] Quit
Select an option: 1
Enter the new task: Finish homework

 Added: 'Finish homework'

====================================================================================================
       MY TO-DO LIST
====================================================================================================
 1. [ ] Buy groceries
 2. [ ] Finish homework
====================================================================================================

Commands: [1] Add  [2] Done  [3] Delete  [4] Quit
Select an option: 2
Enter task number to mark done: 1

 Task marked as complete!

====================================================================================================
       MY TO-DO LIST
====================================================================================================
 1. [x] Buy groceries
 2. [ ] Finish homework
====================================================================================================

Commands: [1] Add  [2] Done  [3] Delete  [4] Quit
Select an option: 4

Saving your tasks... Goodbye!
```

---

## Python Basics Used in This Project

### 1. **Import Statements**
```python
import json
import os
```
- `json`: Handles reading/writing JSON data files
- `os`: Provides file system operations (checking if file exists)
- **Concept**: Standard library modules for file handling

### 2. **Module-Level Constants**
```python
DATA_FILE = "C:\\Documents\\Desktop\\Main_projects\\sample_project\\Python basic projects\\Todo_list\\todo.json"
```
- Defines a constant file path used throughout the program
- Uses uppercase naming convention for constants
- Avoids hardcoding paths in multiple places
- **Concept**: Constants and code maintainability

### 3. **File Path with Escape Characters**
```python
DATA_FILE = "C:\\Documents\\Desktop\\...\\.json"
```
- `\\` represents a single backslash in strings
- Necessary for Windows file paths in Python
- **Concept**: String escape sequences

### 4. **Function Definition**
```python
def load_tasks():
def save_tasks(tasks):
def view_tasks(tasks):
def main():
```
- Multiple functions to organize code
- Each function has a single responsibility
- Functions are reusable and testable
- **Concept**: Function design and modularity

### 5. **Try/Except Block (Exception Handling)**
```python
try:
    with open(DATA_FILE, 'r') as file:
        return json.load(file)
except json.JSONDecodeError:
    return []
```
- `try`: Attempts to load and parse JSON
- `except json.JSONDecodeError`: Catches error if JSON is empty/invalid
- Prevents program crash from corrupted data
- **Concept**: Error handling and robustness

### 6. **Conditional Statement - File Existence Check**
```python
if os.path.exists(DATA_FILE):
```
- `os.path.exists()`: Checks if file exists on disk
- Returns True/False boolean value
- Prevents errors from trying to open non-existent files
- **Concept**: File system operations and conditionals

### 7. **Context Manager - With Statement**
```python
with open(DATA_FILE, 'r') as file:
    return json.load(file)
```
- `with` statement automatically closes file after use
- Even if an error occurs, file is properly closed
- More reliable than manual `file.close()`
- **Concept**: Resource management and context managers

### 8. **JSON Module - load() Function**
```python
return json.load(file)
```
- Reads and parses JSON data from a file
- Converts JSON to Python data structures
- JSON arrays `[]` become Python lists
- JSON objects `{}` become Python dictionaries
- **Concept**: JSON parsing and data serialization

### 9. **JSON Module - dump() Function**
```python
json.dump(tasks, file, indent=4)
```
- Writes Python data structures to file as JSON
- `indent=4`: Formats JSON with 4-space indentation (readable)
- Automatically converts Python types to JSON
- **Concept**: JSON serialization and formatting

### 10. **Lists and List Methods**
```python
return []
tasks.append({"description": new_task_desc, "done": False})
removed_task = tasks.pop(task_num - 1)
```
- Lists store task objects (dictionaries)
- `.append()`: Adds new task to end of list
- `.pop()`: Removes and returns item at index
- **Concept**: Lists, methods, and data structures

### 11. **Dictionaries**
```python
{"description": new_task_desc, "done": False}
task['description']
task['done'] = True
```
- Dictionaries store key-value pairs
- Each task is a dictionary with "description" and "done" keys
- Access values using `dict[key]` syntax
- Can modify dictionary values
- **Concept**: Dictionaries and key-value data structures

### 12. **For Loop with enumerate()**
```python
for index, task in enumerate(tasks, start=1):
    status = "[x]" if task['done'] else "[ ]"
    print(f" {index}. {status} {task['description']}")
```
- `enumerate()`: Gets both index and value from list
- `start=1`: Numbering starts from 1 (not 0)
- Unpacks tuple into `index` and `task`
- **Concept**: Iteration, enumerate, and unpacking

### 13. **Ternary Conditional Expression**
```python
status = "[x]" if task['done'] else "[ ]"
```
- Inline if/else statement: `value_if_true if condition else value_if_false`
- Assigns different status symbols based on task completion
- Makes code concise and readable
- **Concept**: Conditional expressions and ternary operators

### 14. **F-String Formatting**
```python
print(f" {index}. {status} {task['description']}")
print(f"\n Added: '{new_task_desc}'")
```
- Embeds variables and expressions in strings
- `{index}`, `{status}`, `{task['description']}` are replaced with values
- **Concept**: String formatting and interpolation

### 15. **Input Function and String Methods**
```python
choice = input("Select an option: ").strip()
new_task_desc = input("Enter the new task: ").strip()
```
- `input()`: Gets user input as string
- `.strip()`: Removes leading/trailing whitespace
- Prevents issues with accidental spaces
- **Concept**: User input and string methods

### 16. **While True Loop (Infinite Loop)**
```python
while True:
    # menu and options
    if condition:
        break  # exit loop when user quits
```
- `while True`: Creates infinite loop
- Continues until `break` statement is encountered
- Perfect for interactive menu-driven applications
- **Concept**: Loop control and break statement

### 17. **Match Statement (Pattern Matching) - Python 3.10+**
```python
match choice:
    case '1':
        # Add task
    case '2':
        # Mark done
    case '3':
        # Delete task
    case '4' | 'q' | 'quit':
        # Quit
    case _:
        # Invalid choice
```
- Modern alternative to multiple if/elif statements
- `case`: Matches specific values
- `case '4' | 'q' | 'quit':`: Matches multiple values (OR operator `|`)
- `case _`: Default case (matches anything)
- **Concept**: Pattern matching and switch-like logic

### 18. **Type Conversion - int()**
```python
task_num = int(input("Enter task number to delete: "))
```
- Converts user input string to integer
- Necessary because `input()` always returns string
- Used for numeric comparisons and list indexing
- **Concept**: Type conversion and casting

### 19. **Try/Except for Input Validation**
```python
try:
    task_num = int(input("Enter task number to delete: "))
except ValueError:
    print("\n Please enter a valid number.")
```
- `try`: Attempts to convert input to integer
- `except ValueError`: Catches error if input isn't a number
- Validates user input without crashing
- **Concept**: Input validation and error handling

### 20. **Range Checking with Comparison Operators**
```python
if 1 <= task_num <= len(tasks):
    # Valid task number
else:
    # Invalid task number
```
- `<=`: Less than or equal to
- Checks if task number is within valid range
- `len(tasks)`: Gets number of tasks in list
- **Concept**: Range validation and compound comparisons

### 21. **List Indexing and Index Offset**
```python
tasks[task_num - 1]['done'] = True
removed_task = tasks.pop(task_num - 1)
```
- Lists use 0-based indexing (first item is at index 0)
- User numbers tasks starting from 1
- `-1` converts user's 1-based number to 0-based index
- **Concept**: Indexing, offsets, and array access

### 22. **Conditional Data Validation**
```python
if new_task_desc:
    # Add task
else:
    print("\n Task description cannot be empty.")
```
- Empty string is "falsy" in Python
- Non-empty string is "truthy"
- Prevents adding empty tasks
- **Concept**: Truthy/falsy values and validation

### 23. **String Escape Sequences**
```python
print("\n" + "="*100)
```
- `\n`: Newline character
- `\\`: Backslash character
- Makes output more readable and visually organized
- **Concept**: Escape sequences and special characters

### 24. **String Multiplication**
```python
print("="*100)
```
- Repeats string 100 times
- Creates visual separator lines
- **Concept**: String operations

### 25. **Main Block Guard Clause**
```python
if __name__ == "__main__":
    main()
```
- Code only runs when script is executed directly
- Not run if script is imported as a module
- Best practice for Python scripts
- **Concept**: Script execution control

---

## Data Structure: Task Format

Each task is stored as a dictionary with two keys:
```json
{
    "description": "Buy groceries",
    "done": false
}
```

All tasks are stored in a JSON array:
```json
[
    {
        "description": "Buy groceries",
        "done": true
    },
    {
        "description": "Finish homework",
        "done": false
    }
]
```

---

## Python Concepts Summary Table

| Concept | Example | Purpose |
|---------|---------|---------|
| Imports | `import json, os` | Access modules |
| Constants | `DATA_FILE = "..."` | Store fixed values |
| Functions | `def load_tasks():` | Organize code |
| Try/Except | Try/catch errors | Error handling |
| File I/O | `open()`, `with` | Read/write files |
| JSON | `json.load()`, `json.dump()` | Handle JSON data |
| Lists | `tasks.append()`, `tasks.pop()` | Store collections |
| Dictionaries | `{"key": value}` | Store key-value pairs |
| For Loop | `for index, task in enumerate()` | Iterate with index |
| Ternary Op | `value if condition else value` | Inline conditionals |
| While Loop | `while True:` with `break` | Infinite menu loop |
| Match Statement | `match choice: case '1':` | Pattern matching |
| Type Conversion | `int(input())` | Convert data types |
| String Methods | `.strip()` | Transform strings |
| Input Validation | Range checks | Ensure valid data |
| F-Strings | `f"{variable}"` | Format strings |

---

## File Structure
```
Todo_list/
├── main.py          # Main application file
├── todo.json        # Persistent task storage (auto-created)
└── README.md        # This file
```

## Requirements
- Python 3.10 or higher (for `match` statement support)
- No external libraries (uses only Python standard library)
- Write permission in the Todo_list directory (for saving `todo.json`)

## Menu Options
- **[1] Add**: Create a new task
- **[2] Done**: Mark a task as complete (shows `[x]` instead of `[ ]`)
- **[3] Delete**: Remove a task from the list
- **[4] Quit**: Exit the application (you can also type `q` or `quit`)

## Tips
- Tasks are numbered starting from 1 (not 0)
- Completed tasks show with `[x]`, incomplete show with `[ ]`
- Tasks are automatically saved to `todo.json` after each change
- The application creates `todo.json` automatically if it doesn't exist
- If `todo.json` is corrupted, it's safely handled and starts fresh

## Error Handling
- **Empty JSON file**: Handled gracefully, starts with empty list
- **Invalid task number**: Shows error message and asks for retry
- **Non-numeric input**: Caught with try/except, user prompted again
- **Empty task description**: Validation prevents adding empty tasks

## Learning Outcomes
This project demonstrates:
- File I/O and JSON handling
- Data persistence and serialization
- Exception handling and error recovery
- Menu-driven application design
- List and dictionary operations
- User input validation
- Control flow with loops and conditionals
- Modern Python features (match statement)
- Code organization with functions
- Defensive programming practices

## Possible Enhancements
- Add task categories or tags
- Implement due dates for tasks
- Add priority levels (high, medium, low)
- Search functionality
- Edit existing tasks
- Sort tasks by completion status or priority
- Set reminders or notifications
- Create a GUI version
- Add task filtering options
- Implement undo/redo functionality

## Bug Fixed
- **JSONDecodeError**: Added error handling for empty or corrupted JSON files. The application now gracefully handles empty `todo.json` files instead of crashing.

