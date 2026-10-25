def cli():
    print(" \t🔶 WELCOME TO MY CODE ALPHA PYTHON PROGRAMMING INTERNSHIP PROJECT 🔶 \n")

    task_number = int(input('''PLEASE ENTER THE TASK NUMBER YOU WANT TO RUN (1-5) :
        \t 1. HANGMAN GAME
        \t 2. TASK 2
        \t 3. TASK 3
        \t 4. TASK 4
        \t 5. EXIT
    ''').strip())

    if task_number == 1:
        from src.TASK1 import taskone
        taskone()
    elif task_number == 2:
        from src.TASK2 import tasktwo
        tasktwo()
    elif task_number == 3:
        from src.TASK3 import taskthree
        taskthree()
    elif task_number == 4:
        from src.TASK4 import taskfour
        taskfour()
    elif task_number == 5:
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Invalid task number. Please enter a number between 1 and 5.")
        cli()


