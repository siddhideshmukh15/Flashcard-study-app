
import random

print("===== Flashcard Study App =====")

flashcards = {
    "What is CPU?": "Central Processing Unit",
    "What is RAM?": "Random Access Memory",
    "What is ROM?": "Read Only Memory",
    "What is Python?": "A programming language",
    "What is a variable?": "A named storage location for data"
}

while True:
    print("\n1. Study Flashcards")
    print("2. Take Quiz")
    print("3. Add Flashcard")
    print("4. View Flashcards")
    print("5. Delete Flashcard")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not flashcards:
            print("No flashcards available!")
        else:
            for question, answer in flashcards.items():
                print("\nQuestion:", question)
                input("Press Enter to reveal answer...")
                print("Answer:", answer)

    elif choice == "2":
        if not flashcards:
            print("No flashcards available!")
            continue

        score = 0
        questions = list(flashcards.items())
        random.shuffle(questions)

        for question, answer in questions:
            print("\nQuestion:", question)
            user_answer = input("Your answer: ")

            if user_answer.strip().lower() == answer.lower():
                print("Correct!")
                score += 1
            else:
                print("Correct answer:", answer)

        print("\nFinal Score:", score, "/", len(questions))

    elif choice == "3":
        question = input("Enter your question: ").strip()
        answer = input("Enter the answer: ").strip()

        if question and answer:
            flashcards[question] = answer
            print("Flashcard added!")
        else:
            print("Question and answer cannot be empty!")

    elif choice == "4":
        if flashcards:
            for i, (question, answer) in enumerate(
                flashcards.items(), 1
            ):
                print(f"\n{i}. {question}")
                print("Answer:", answer)
        else:
            print("No flashcards available!")

    elif choice == "5":
        questions = list(flashcards.keys())

        if not questions:
            print("No flashcards to delete!")
            continue

        for i, question in enumerate(questions, 1):
            print(f"{i}. {question}")

        number = input("Enter question number to delete: ")

        if number.isdigit() and 1 <= int(number) <= len(questions):
            del flashcards[questions[int(number) - 1]]
            print("Flashcard deleted!")
        else:
            print("Invalid question number!")

    elif choice == "6":
        print("Happy learning! Goodbye.")
        break

    else:
        print("Invalid choice! Try again.")

