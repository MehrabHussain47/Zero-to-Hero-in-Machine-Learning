class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")        
        priority = input("Enter priority (High/Medium/Low): ").capitalize()

        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority! Setting default: Low")
            priority = "Low"

        task = {
            "title": title,
            "description": description,
            "priority": priority
        }

        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            return

        print("\n===== Your Tasks =====")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['title']} - {task['description']} [{task['priority']} Priority]")

    def delete_task(self):
        self.view_tasks()

        if not self.tasks:
            return

        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(self.tasks):
                removed = self.tasks.pop(index)
                print(f"Deleted task: {removed['title']}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

    def update_priority(self):
        self.view_tasks()

        if not self.tasks:
            return

        try:
            index = int(input("Enter task number to update priority: ")) - 1

            if 0 <= index < len(self.tasks):
                new_priority = input("Enter new priority (High/Medium/Low): ").capitalize()

                if new_priority not in ["High", "Medium", "Low"]:
                    print("Invalid priority!")
                    return

                self.tasks[index]["priority"] = new_priority
                print("Task priority updated successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")


manager = TaskManager()

while True:
    print("\n===== Task Tracker =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task Priority")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        manager.add_task()
    elif choice == "2":
        manager.view_tasks()
    elif choice == "3":
        manager.delete_task()
    elif choice == "4":
        manager.update_priority()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")