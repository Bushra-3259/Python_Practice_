#Plans on how to start and what to do in the project
# list of questions
# store the answers
# randomly pick questions
# ask the questions
# see if they are correct
# keep track of the score
# tell the user their score

import random # Import the random module which provides functions for random selections or random numbers

# Creating a dictionary called 'questions' where:
# - Keys are the trivia questions
# - Values are the correct answers to those questions
questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}

# Defining a function called 'python_trivia_game' that will run our quiz game
def python_trivia_game():
    questions_list = list(questions.keys()) # Converting the dictionary keys (questions) into a list and storing it in 'questions_list'
    total_questions = 5 # Deciding how many questions to ask in one game session
    score = 0 # Initializing the player's score to 0

    selected_questions = random.sample(questions_list, total_questions)  # Randomly selecting 5 questions from the full list without repeating any
    
     # Using a for loop to go through each of the selected questions
    for index, question in enumerate(selected_questions):
        print(f"{index+1}.{question}") # Displaying the question number (starting from 1) and the question itself
        user_answer = input("Your answer: ").lower().strip() # Taking the user's answer as input, converting it to lowercase and removing extra spaces

        correct_answer = questions[question]  # Retrieving the correct answer for the current question from the dictionary

        if user_answer == correct_answer.lower(): # Comparing the user's answer with the correct answer (also converting correct answer to lowercase for fair comparison)
            print("Correct!\n") # If the answer is correct, print a message and increase the score
            score += 1 
        else:
            print(f"Wrong. The correct answer is: {correct_answer}.\n")  # If the answer is wrong, print the correct answer

    print(f"Game over. Your final score is: {score}/{total_questions}") # After all questions are done, print the final score

python_trivia_game() # Calling the function to start the trivia game