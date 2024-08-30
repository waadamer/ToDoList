
print("Welcome to the To-Do List Manager!")

tasks = []

while True:
    print(
        "\n1. View to-do list \n2. Add a task \n3. Mark a task as completed \n4. Delete a task \n5. Exit"
    )

    option = input("Choose an option: ")

    if option == "1":
        if not tasks:
            print("Your To-Do List is empty.")
        else:
            print("Your To-Do List:")
            for i, toDo in enumerate(tasks, start=1):
                status = "Completed" if toDo["completed"] else "Not Completed"
                print(f"{i}. {toDo['name']} - {status}")

    elif option == "2":
        taskName = input("Enter the new task: ")
        task = {"name": taskName, "completed": False}
        tasks.append(task)
        print("Task added!")

    elif option == "3":
        taskNum = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= taskNum < len(tasks):
            tasks[taskNum]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    elif option == "4":
        taskNum = int(input("Enter the task number to delete: ")) - 1
        if 0 <= taskNum < len(tasks):
            tasks.pop(taskNum)
            print("Task deleted!")
        else:
            print("Invalid task number.")

    elif option == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please try again.")
