from manager import TaskManager
from task import Task
from observer import EmailNotifier, SMSNotifier
from strategy import SortByName, SortByPriority, SortByNameLength, TaskSorter

def main():
    manager = TaskManager()

    email = EmailNotifier()
    sms = SMSNotifier()

    while True:
        print("\n1. Add Task")
        print("2. Change Task Status")
        print("3. View Tasks")
        print("4. Sort Tasks")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Task name: ")
            priority = int(input("Priority (1-5): "))

            task = Task(name)
            task.priority = priority

            # Attach observers
            task.attach(email)
            task.attach(sms)

            manager.add_task(task)
            print("Task added!")

        elif choice == "2":
            for i, t in enumerate(manager.tasks):
                print(f"{i}: {t.name}")

            idx = int(input("Select task index: "))
            status = input("Enter new status: ")

            manager.tasks[idx].change_status(status)

        elif choice == "3":
            for t in manager.tasks:
                print(f"{t.name} | Priority: {t.priority}")

        elif choice == "4":
            print("\n1. By Name")
            print("2. By Priority")
            print("3. By Name Length")

            opt = input("Choose sorting: ")

            if opt == "1":
                sorter = TaskSorter(SortByName())
            elif opt == "2":
                sorter = TaskSorter(SortByPriority())
            else:
                sorter = TaskSorter(SortByNameLength())

            sorted_tasks = sorter.sort_tasks(manager.tasks)

            print("\nSorted Tasks:")
            for t in sorted_tasks:
                print(f"{t.name} | Priority: {t.priority}")

        elif choice == "5":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()