import json
from pathlib import Path

def add_task():
    task = input("Enter The Task:")
    with open("tasks.json") as f:
        tasks = json.load(f)
    tasks.append(task) 
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

def view_task():
    with open("tasks.json") as f:
        tasks = json.load(f)
    if not tasks:
        print("No tasks found")
    else:
        print("Tasks:")
        for i in tasks:
            print(f"- {i}")

def delete_task():
    with open("tasks.json") as f:
        tasks = json.load(f)
    if not tasks:
        print("No tasks found")
    else:
        for i, x in enumerate(tasks, start=1):
            print(f"{i}. {x}")
        inp = int(input("Enter number of task to delete: "))
        tasks.pop(inp-1)
        with open("tasks.json", "w") as f:
            json.dump(tasks, f, indent=2)

def main():
    file = Path("tasks.json")
    if not file.exists():
        with open("tasks.json", "w") as f:
            json.dump([], f)

    print("TODO LIST")
    inp = int(input("Choose Operation: \n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit\n"))

    if inp == 1:
        add_task()
    elif inp == 2:
        view_task()
    elif inp == 3:
        delete_task()
    elif inp == 4:
        exit()

while True: 
    main()