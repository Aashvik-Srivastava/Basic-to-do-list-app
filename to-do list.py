import os

file_name = "tasks.txt"


tasks = []
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line != "":
                tasks.append(line)

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_task = input("Enter new task: ")
        if new_task != "":
            tasks.append(new_task)
            print("Task added!")
