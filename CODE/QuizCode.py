# Define the quiz questions and options
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    }
]

# Function to run the quiz game
def run_quiz():
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        
        user_answer = input("Select the correct option (1/2/3/4): ")
        if q["options"][int(user_answer) - 1] == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print(f"\nYour final score is: {score}/{len(questions)}")

# Run the quiz
run_quiz()
