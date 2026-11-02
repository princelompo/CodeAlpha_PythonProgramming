


print("\t 🔶 WELCOME TO TASK 3 : Tasks Automation\n ")

def automation():
    print("\t 🔹 TASK 3 : Automation")
    print("\t 🔹 TASK 3.1 : Automation of File Handling")
    print("\t 🔹 TASK 3.2 : Automation of Mails ")
    print("\t 🔹 TASK 3.3 : Automation of Web Scraping")

    answer = input("\t 🔹 Please select a task to automate (1-3) or 4 to exit: ")

    if answer == "1":
        import os
        import shutil
        print("\t 🔹 TASK 3.1 : Automation of File Handling : Move all .jpg files to another folder\n ")
        path = input("\t 🔹 Please enter the source folder path: ")
        files = [f for f in os.listdir(path) if f.endswith('.jpg')]
        if not files:
            print("\t 🔹 No .jpg files found in the source folder.")
        else:
            dest = os.path.join(path, 'jpg_files')
            os.makedirs(dest, exist_ok=True)
            for f in files:
                shutil.move(os.path.join(path, f), os.path.join(dest, f))
        print("\t 🔹 All .jpg files have been moved to the folder: ", dest);

    elif answer == "2":
        import re
        print("\t 🔹 TASK 3.2 : Automation of Mails : Extract email addresses from a text file\n ")
        file_path = input("\t 🔹 Please enter the path of the text file: ")
        with open(file_path, 'r') as file:
            content = file.read()
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)
        new_file_path = input("\t 🔹 Please enter the path to save the extracted email addresses: ")
        with open(new_file_path, 'w') as file:
            for email in emails:
                file.write(email + '\n')
        print("\t 🔹 Extracted email addresses: ", emails)

    elif answer == "3":
        import requests
        print("\t 🔹 TASK 3.3 : Automation of Web Scraping : Scrape the title of a webpage and save it to a file\n ")
        url = input("\t 🔹 Please enter the URL of the webpage: ")
        response = requests.get(url)
        title = response.title
        file_path = input("\t 🔹 Please enter the path to save the scraped title: ")
        with open(file_path, 'w') as file:
            file.write(title)
        print("\t 🔹 Scraped title: ", title)

    elif answer == "4":
        print("\t 🔹 Exiting the program.")

    else:
        print("\t 🔹 Invalid selection. Please select a task between 1 and 3.\n")
        automation()

    

