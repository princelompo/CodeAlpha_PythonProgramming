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
        from src.utils.taskone import hangman
        hangman()
    elif task_number == 2:
        from src.utils.tasktwo import task_two
        task_two()
    elif task_number == 3:
        from src.utils.taskthree import task_three
        task_three()
    elif task_number == 4:
        from src.utils.taskfour import task_four
        task_four()
    elif task_number == 5:
        print(" THANK YOU FOR USING MY CODE ALPHA PYTHON PROGRAMMING INTERNSHIP PROJECT. GOODBYE! \n")
    else:
        print(" INVALID TASK NUMBER. PLEASE ENTER A VALID TASK NUMBER (1-5). \n")