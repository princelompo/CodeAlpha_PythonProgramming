print(" \n\t 🔶 WELCOME TO TASK 4 : A SIMPLE I/O CHATBOT\n ")

def chatbot():
    print("\t 🔹 TASK 4 : A SIMPLE I/O CHATBOT")
    print("\t 🔹 TASK 4.1 : Chatbot for Greetings")
    print("\t 🔹 TASK 4.2 : Chatbot for Farewells")
    print("\t 🔹 TASK 4.3 : Chatbot for Small Talk")

    answer = input("\t 🔹 Please select a chatbot task (1-3) or 4 to exit: ")

    if answer == "1":
        print("\t 🔹 TASK 4.1 : Chatbot for Greetings\n ")
        name = input("\t 🔹 Please enter your name: ")
        print(f"\t 🔹 Hello, {name}! How can I assist you today?")

    elif answer == "2":
        print("\t 🔹 TASK 4.2 : Chatbot for Farewells\n ")
        name = input("\t 🔹 Please enter your name: ")
        print(f"\t 🔹 Goodbye, {name}! Have a great day!")

    elif answer == "3":
        print("\t 🔹 TASK 4.3 : Chatbot for Small Talk\n ")
        topic = input("\t 🔹 Please enter a topic for small talk: ")
        print(f"\t 🔹 That's interesting! Let's talk about {topic}.")

    elif answer == "4":
        print("\t 🔹 Exiting the chatbot.")

    else:
        print("\t 🔹 Invalid selection. Please select a task between 1 and 3.\n")
        chatbot()
