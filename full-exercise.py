#Variables - list that stores all the tasks as "strings"
todo_list = ["grab lunch box", "pack snacks", "pack drink", "pack water bottle"]

#for loop
def show_tasks():
    print("Show tasks:")
    for task in todo_list:
        print("-" + task)

#while loop
while True:
    print("What woud you like to do?")
    print("1. Add a task:")
    print("2. Show tasks:")
    print("3. Quit")

    choice = input("Please choose an option (1-3): ")

#if input is 1 or 2 or 3
    if choice == "1":
        new_task = input("Add a task:")
        todo_list.append(new_task)
        print("Task added!")    
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        print("See ya!")
        break
    else:
        print("Please choose a different option...")




