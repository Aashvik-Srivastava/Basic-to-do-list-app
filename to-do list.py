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
elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            count = 1
            for task in tasks:
                print(str(count) + ". " + task)
                count += 1

elif choice == "3":
        number = input("Enter task number to remove: ")
        if number.isdigit():
            number = int(number)
            if number >= 1 and number <= len(tasks):
                removed = tasks.pop(number - 1)
                print("Removed:", removed)
            else:
                print("Invalid task number.")
        else:
            print("Please enter a valid number.")

  
    elif choice == "4":
        # Save tasks before exiting
        with open(file_name, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")                


