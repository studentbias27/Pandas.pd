'''Daily System'''

name = input("Enter your name: ")
print(f"Hello {name}, Welcome to the Daily System.")

tasks = []

def add_task(task):
    tasks.append(task)
    
    #print(f"Added: {task}")

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")        
        
print("Today's tasks are:")

add_task("Wake at 6 AM.")
add_task("1 Hour Physical training.")
add_task("4 Hour Study.")
add_task("Drink 3 Liter Water.")
add_task("1 Hour Book reading.")
add_task("00:00 time for bed.")



show_tasks()
