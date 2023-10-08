import requests
import random

#  Defining function for game playing

def play_game_kb(username, kb):
    print("Hello,", username, "welcome to the QUIZ game")
    print("All the Best for the Game :>")
    score = 0
    random.shuffle(kb)
    exit = False
    for qset in kb:
        current_question = qset['question']
        correct_answer = qset['correctAnswer']
        current_question_options = qset['incorrectAnswers']
        if correct_answer not in current_question_options:
            current_question_options.append(correct_answer)
        random.shuffle(current_question_options)
        print("Question:", current_question)
        user_options = list()
        for index, each_options in enumerate(current_question_options):
            print(index+1, ") ", each_options, sep='')
            user_options.append(str(index+1))
        exit_option = len(current_question_options)+1
        print(exit_option, ") ", 'Exit', sep='')
        user_options.append(str(exit_option))

        user_answer_index = 0
        option_list = ','.join(user_options)

        while str(user_answer_index) not in user_options:
            try:
                user_answer_index = int(input(f"Please enter your choice({option_list}): "))
            except Exception as e:
                print(f"Invalid input => [{e}]")
        if user_answer_index == exit_option:
            print("Bye\n")
            exit = True
            break
        user_answer = current_question_options[user_answer_index-1]
        if user_answer == correct_answer:
            print("correct answer\n")
            score = score + 100
        else:
            print("Wrong Answer!!! \n => Correct answer is", correct_answer)
            break
    print("Your final score is", score)
    return score, exit


# Defining function for viewing the score

def view_scores(names_and_scores):
    for name, score in names_and_scores.items():
        print(name, "has scored", score)

# Defining the function for start of the score

def quiz_kb():
    names_and_scores = dict()
    while True:
        print("\nWelcome to the quiz game")
        print("1) Play\n2) View Scores\n3) Exit")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            username = ''
            while username.strip() == "":
                username = input("Please enter your name: ")
            knowledge_base = setup_kb()
            score, exit = play_game_kb(username, knowledge_base)
            names_and_scores[username] = score
            if exit:
                break

        elif choice == 2:
            view_scores(names_and_scores)
        elif choice == 3:
            break
        else:
            print("Your choice is not correct")


# get quiz questions
def setup_kb():
    knowledge_base = list()
    qset = {
        "category": "Programming",
        "id": "",
        "correctAnswer": "Guido Van",
        "incorrectAnswers": [
        "Dennis Ritchie",
        "Alan Frank",
        "Albert"
        ],
        "question": "Who is the developer of Python Language?",
        "tags": [
        "technical",
        "programming",
        "python"
        ],
        "type": "Multiple Choice",
        "difficulty": "medium",
        "regions": [],
        "isNiche": False
    }
    response = requests.get('https://the-trivia-api.com/api/questions/')
    if response.status_code == 200:
        knowledge_base = response.json()
    else:
        knowledge_base.append(qset)    
    return knowledge_base

#  Program execution starts from here

if __name__ == '__main__':
    quiz_kb()
