def add_task(tasks, task):
    tasks.append(task)
    print("Task added!")

def show_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks!")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def remove_task(tasks, number):
    tasks.pop(number - 1)
    print("Task removed!")

tasks = []

while True:
    print("\n1. Add task\n2. Show tasks\n3. Remove task\n4. Quit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Task name: ")
        add_task(tasks, task)
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        number = int(input("Which number? "))
        remove_task(tasks, number)
    elif choice == "4":
        break