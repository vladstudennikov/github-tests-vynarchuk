from service import TaskService

def main():
    service = TaskService()

    while True:
        print("1 - Add task")
        print("2 - Show tasks")
        print("3 - Exit\n")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            try:
                service.add_task(title)
                print("Task added\n")
            except Exception as e:
                print(f"Error: {e}\n")

        elif choice == "2":
            tasks = service.get_tasks()
            if not tasks:
                print("No tasks\n")
            else:
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task.title}\n")

        elif choice == "3":
            break

        else:
            print("Invalid option\n")

if __name__ == "__main__":
    main()