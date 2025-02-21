import os
import sys
import platform

def shut_down():
    if platform.system() == 'Windows':
        os.system('shutdown /s /t 1')
    elif platform.system() == 'Darwin':  # macOS
        os.system('shutdown -h now')
    elif platform.system() == 'Linux':
        os.system('shutdown now')
    else:
        print("Unsupported operating system. Cannot shut down the computer.")
        sys.exit()

def game():
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Who wrote 'Hamlet'?", "answer": "William Shakespeare"},
    {"question": "What is the smallest planet in our solar system?", "answer": "Mercury"},
    {"question": "How many continents are there on Earth?", "answer": "7"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the square root of 144?", "answer": "12"},
    {"question": "Which ocean is the largest?", "answer": "Pacific Ocean"},
    {"question": "Who discovered penicillin?", "answer": "Alexander Fleming"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is the largest mammal?", "answer": "Blue Whale"},
    {"question": "Who developed the theory of relativity?", "answer": "Albert Einstein"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
    {"question": "Which country gifted the Statue of Liberty to the USA?", "answer": "France"},
    {"question": "How many players are there in a standard soccer team?", "answer": "11"},
    {"question": "What is the national flower of Japan?", "answer": "Cherry Blossom"},
    {"question": "Which is the longest river in the world?", "answer": "Nile"},
    {"question": "What is the speed of light in vacuum?", "answer": "299,792,458 meters per second"},
    {"question": "Which gas do plants absorb from the atmosphere?", "answer": "Carbon Dioxide"},
    {"question": "Who was the first person to walk on the moon?", "answer": "Neil Armstrong"},
    {"question": "What is the chemical symbol for oxygen?", "answer": "O"},
    {"question": "Which is the tallest mountain in the world?", "answer": "Mount Everest"},
    {"question": "Who invented the telephone?", "answer": "Alexander Graham Bell"},
    {"question": "What is the national animal of Australia?", "answer": "Kangaroo"},
    {"question": "How many bones are there in an adult human body?", "answer": "206"},
    {"question": "What is the freezing point of water in Celsius?", "answer": "0"},
    {"question": "Which bird is known for its ability to mimic human speech?", "answer": "Parrot"},
    {"question": "Who painted the Sistine Chapel ceiling?", "answer": "Michelangelo"},
    {"question": "What is the currency of the United Kingdom?", "answer": "Pound Sterling"}
    ]

    score = 0
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question['question']}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == question['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. Shutting down the computer...")
            shut_down()
            break

    print(f"Your final score is {score}/{len(questions)}")

game()