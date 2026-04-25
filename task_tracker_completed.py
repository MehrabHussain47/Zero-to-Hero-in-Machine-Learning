class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        print("\n--- Add New Task ---")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        
        new_task = {
            "title": title,
            "description": description,
            "completed": False
        }
        
        self.tasks.append(new_task)
        print("Task added successfully!")

    def view_tasks(self):
        print("\n--- Your Tasks ---")
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{index}. {task['title']} - {task['description']} [{status}]")

    def delete_task(self):
        self.view_tasks()
        if self.tasks:
            try:
                task_num = int(input("\nEnter the task number to delete: "))
                if 1 <= task_num <= len(self.tasks):
                    removed_task = self.tasks.pop(task_num - 1)
                    print(f"Task '{removed_task['title']}' deleted successfully!")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    def mark_completed(self):
        self.view_tasks()
        if not self.tasks:
            return

        try:
            task_num = int(input("\nEnter task number to mark as completed: "))
            if 1 <= task_num <= len(self.tasks):
                self.tasks[task_num - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    manager = TaskManager()

    while True:
        print("\n===== Task Tracker =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            manager.add_task()
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            manager.delete_task()
        elif choice == '4':
            manager.mark_completed()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select 1-5.")

if __name__ == "__main__":
    main()