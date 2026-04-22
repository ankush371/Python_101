import json
import os

DATA_FILE = "C:\\Documents\\Desktop\\Main_projects\\sample_project\\Python basic projects\\Todo_list\\todo.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    print("\n" + "="*100)
    print("       MY TO-DO LIST")
    print("="*100)
    
    if not tasks:
        print(" Nothing to do! You're all caught up.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "[x]" if task['done'] else "[ ]"
            print(f" {index}. {status} {task['description']}")
            
    print("="*100 + "\n")

def main():
    tasks = load_tasks()

    while True:
        view_tasks(tasks)
        print("Commands: [1] Add  [2] Done  [3] Delete  [4] Quit")
        choice = input("Select an option: ").strip()

        match choice:
            case '1':
                # ADD TASK
                new_task_desc = input("Enter the new task: ").strip()
                if new_task_desc:
                    tasks.append({"description": new_task_desc, "done": False})
                    save_tasks(tasks)
                    print(f"\n Added: '{new_task_desc}'")
                else:
                    print("\n Task description cannot be empty.")

            case '2':
                # MARK DONE
                try:
                    task_num = int(input("Enter task number to mark done: "))
                    if 1 <= task_num <= len(tasks):
                        tasks[task_num - 1]['done'] = True
                        save_tasks(tasks)
                        print("\n Task marked as complete!")
                    else:
                        print("\n Invalid task number.")
                except ValueError:
                    print("\n Please enter a valid number.")

            case '3':
                # DELETE TASK
                try:
                    task_num = int(input("Enter task number to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        save_tasks(tasks)
                        print(f"\n Deleted: '{removed_task['description']}'")
                    else:
                        print("\n Invalid task number.")
                except ValueError:
                    print("\n Please enter a valid number.")

            case '4' | 'q' | 'quit':
                # QUIT
                print("\nSaving your tasks... Goodbye!")
                break

            case _:
                print("\n Invalid choice. Please press 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()