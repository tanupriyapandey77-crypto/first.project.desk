# todo.py

tasks = []

def show_menu():
    print("\n==== TO-DO LIST APP ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print(f"'{task}' added!")

    elif choice == '2':
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks yet!")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == '3':
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f" '{removed}' removed!")
        else:
            print("Invalid task number!")

    elif choice == '4':
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice! Try again.")
