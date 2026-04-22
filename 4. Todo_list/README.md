# Todo List Application

## Overview
**Todo List** is an interactive command-line application that helps you manage your daily tasks. Add, mark tasks as complete, delete tasks, and automatically save everything to a JSON file. Your tasks persist between sessions, so you never lose your to-do list!


## How to Run
```bash
python main.py
```

## Python Basics Used in This Project

### 1. **Module-Level Constants**
```python
DATA_FILE = "path\\todo.json"
```
- Defines a constant file path used throughout the program
- Uses uppercase naming convention for constants
- Avoids hardcoding paths in multiple places
- **Concept**: Constants and code maintainability

### 2. **File Path with Escape Characters**
```python
DATA_FILE = "C:\\Documents\\Desktop\\...\\.json"
```
- `\\` represents a single backslash in strings
- Necessary for Windows file paths in Python
- **Concept**: String escape sequences

### 3. **Function Definition**
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

### 4. **Try/Except Block (Exception Handling)**
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

### 5. **Conditional Statement - File Existence Check**
```python
if os.path.exists(DATA_FILE):
```
- `os.path.exists()`: Checks if file exists on disk
- Returns True/False boolean value
- Prevents errors from trying to open non-existent files
- **Concept**: File system operations and conditionals

### 6. **Context Manager - With Statement**
```python
with open(DATA_FILE, 'r') as file:
    return json.load(file)
```
- `with` statement automatically closes file after use
- Even if an error occurs, file is properly closed
- More reliable than manual `file.close()`
- **Concept**: Resource management and context managers

### 7. **JSON Module - load() Function**
```python
return json.load(file)
```
- Reads and parses JSON data from a file
- Converts JSON to Python data structures
- JSON arrays `[]` become Python lists
- JSON objects `{}` become Python dictionaries
- **Concept**: JSON parsing and data serialization

### 8. **JSON Module - dump() Function**
```python
json.dump(tasks, file, indent=4)
```
- Writes Python data structures to file as JSON
- `indent=4`: Formats JSON with 4-space indentation (readable)
- Automatically converts Python types to JSON
- **Concept**: JSON serialization and formatting

### 9. **Lists and List Methods**
```python
return []
tasks.append({"description": new_task_desc, "done": False})
removed_task = tasks.pop(task_num - 1)
```
- Lists store task objects (dictionaries)
- `.append()`: Adds new task to end of list
- `.pop()`: Removes and returns item at index
- **Concept**: Lists, methods, and data structures

### 10. **Dictionaries**
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

### 11. **For Loop with enumerate()**
```python
for index, task in enumerate(tasks, start=1):
    status = "[x]" if task['done'] else "[ ]"
    print(f" {index}. {status} {task['description']}")
```
- `enumerate()`: Gets both index and value from list
- `start=1`: Numbering starts from 1 (not 0)
- Unpacks tuple into `index` and `task`
- **Concept**: Iteration, enumerate, and unpacking

### 12. **Ternary Conditional Expression**
```python
status = "[x]" if task['done'] else "[ ]"
```
- Inline if/else statement: `value_if_true if condition else value_if_false`
- Assigns different status symbols based on task completion
- Makes code concise and readable
- **Concept**: Conditional expressions and ternary operators


### 13. **Match Statement (Pattern Matching) - Python 3.10+**
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



### 14. **List Indexing and Index Offset**
```python
tasks[task_num - 1]['done'] = True
removed_task = tasks.pop(task_num - 1)
```
- Lists use 0-based indexing (first item is at index 0)
- User numbers tasks starting from 1
- `-1` converts user's 1-based number to 0-based index
- **Concept**: Indexing, offsets, and array access

### 15. **Conditional Data Validation**
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


## Requirements
- Python 3.10 or higher (for `match` statement support)
- No external libraries (uses only Python standard library)
- Write permission in the Todo_list directory (for saving `todo.json`)

## Menu Options
- **[1] Add**: Create a new task
- **[2] Done**: Mark a task as complete (shows `[x]` instead of `[ ]`)
- **[3] Delete**: Remove a task from the list
- **[4] Quit**: Exit the application (you can also type `q` or `quit`)


## Bug Fixed
- **JSONDecodeError**: Added error handling for empty or corrupted JSON files. The application now gracefully handles empty `todo.json` files instead of crashing.

