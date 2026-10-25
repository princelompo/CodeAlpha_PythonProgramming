import random


print(" \t🔶 WELCOME TO TASK 1 : A SIMPLE TEXT-BASED HANG-MAN GAME 🔶 \n")

print(" RULE : GUESS THE WORD ONE LETTER AT A TIME IN 6 ATTEMPTS OR LESS TO WIN THE GAME \n")

def hangman():
    words = ["python", "programming", "code", "codealpha", "game", "project"]
    word = random.choice(words)
    attempts = 6
    all_words = ""

    while attempts > 0:
        guessed = input(" GUESS A LETTER : ").lower().strip()
        if guessed in word:
            print(f" ✅ GOOD JOB! '{guessed}' IS IN THE WORD.")
            all_words += guessed
        if guessed not in word:
            attempts -= 1
            print(f" ❌ SORRY! '{guessed}' IS NOT IN THE WORD. ATTEMPTS LEFT: {attempts}")

        if attempts == 0:
            print(f" 💀 GAME OVER! THE WORD WAS '{word.upper()}'.\n")
            answer = input(" DO YOU WANT TO PLAY AGAIN? (Y/N): ").lower().strip()
            if answer == 'y':
                hangman()
            else:
                print(" THANK YOU FOR PLAYING! GOODBYE! \n")
                break

        if all(letter in all_words for letter in word):
            print(f" 🎉 CONGRATULATIONS! YOU GUESSED THE WORD '{word.upper()}' CORRECTLY!\n")
            answer = input(" DO YOU WANT TO PLAY AGAIN? (Y/N): ").lower().strip()
            if answer == 'y':
                hangman()
            else:
                print(" THANK YOU FOR PLAYING! GOODBYE! \n")
                break
            