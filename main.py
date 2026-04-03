from service import TaskService

def main():
    service = TaskService()

    while True:
        print("\n1 - Add task")
        print("2 - Show tasks")
        print("3 - Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Enter task title: ")
            try:
                service.add_task(title)
                print("Task added")
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            tasks = service.get_tasks()
            if not tasks:
                print("No tasks")
            else:
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task.title}")

        elif choice == "3":
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()