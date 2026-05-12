def ask_question(question, correct_answer):
    answer = input(question)
    if answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Wrong! The answer was:", correct_answer)
        return False

def play_quiz():
    score = 0
    questions = [
        ("What is the capital of France? ", "paris"),
        ("What is 5 + 3? ", "8"),
        ("What color is the sky? ", "blue"),
        ("How many days are in a week? ", "7"),
    ]

    print("Welcome to the Quiz!")
    print("-------------------")

    for question, answer in questions:
        if ask_question(question, answer):
            score += 1

    print("-------------------")
    print(f"You got {score} out of {len(questions)} correct!")

    if score == len(questions):
        print("Perfect score!")
    elif score >= len(questions) / 2:
        print("Not bad!")
    else:
        print("Better luck next time!")

play_quiz()