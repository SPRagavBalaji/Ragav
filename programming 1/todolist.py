def add(todo):
    task = input("Enter task: ").strip()
    if not task:
        print("Task cannot be empty.")
    elif task in todo:
        print("Task already exists.")
    else:
        todo[task] = False
        print("Task added!")

def show(todo):
    if not todo:
        print("No tasks.")
    else:
        for task, status in todo.items():
            if todo[task]==False:
                stat="Pending"
            else:
                stat="Done"
            print(f"{task} - {stat}")

def done(todo):
    task = input("Enter exact task name to mark done: ").strip()
    if task in todo:
        todo[task] = True
        print("Task marked as done!")
    else:
        print("No such task.")

def remove(todo):
    task = input("Enter exact task name to remove: ").strip()
    if task in todo:
        del todo[task]
        print("Removed:", task)
    else:
        print("No such task.")

def main():
    todo = {}
    while True:
        cmd = input("add/show/done/remove/quit: ").strip().lower()
        if cmd == "add":
            add(todo)
        elif cmd == "show":
            show(todo)
        elif cmd == "done":
            done(todo)
        elif cmd == "remove":
            remove(todo)
        elif cmd == "quit":
            print("Bye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
