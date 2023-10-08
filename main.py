import subprocess


def main():
    # Start an infinite loop to keep displaying the menu until the user decides to quit.
    while True:
        # Printing the options for the user to select the game.
        print("Choose a game to play:")
        print("1. Mastermind")
        print("2. Jumbled Word Game")
        print("3. Trivia Quiz")
        print("4. Quit")

        # Taking the user's choice.
        choice = input("Enter your choice (1/2/3/4): ")

        # Based on the user's choice, run the corresponding game using subprocess.
        # subprocess.run() is used to run shell commands, in this case, to execute the Python game files.

        if choice == "1":
            # Run the mastermind game.
            subprocess.run(["python", "mastermind.py"])
        elif choice == "2":
            # Run the jumbled word game.
            subprocess.run(["python", "jumbled_word_game.py"])
        elif choice == "3":
            # Run the quiz game.
            subprocess.run(["python", "quiz_game.py"])
        elif choice == "4":
            # Exit the loop, thereby ending the program.
            print("Thanks for playing!")
            break
        else:
            # If the user enters a choice not listed in the menu, inform them and display the menu again.
            print("Invalid choice. Please choose again.")


# The code within this conditional block will only execute if main.py is run directly (and not imported elsewhere).
if __name__ == "__main__":
    main()
