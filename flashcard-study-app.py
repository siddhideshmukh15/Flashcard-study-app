print("==== flashcard study app ====")
flashcards={
    "what is cpu?":"Central Processing Unit",
    "What is RAM?":"Random Acess Memory",
    "What is ROM?":"Read only Memory",
    "What is python?":"A programming language",
    "What is variable?":"A named storage location for data"
}
while True:
    print("\n1. Study Flashcards")
    print("2.Add Flashcard")
    print("3. View All Flashcards")
    print("4.Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        if not flashcards:
            print("No flashcards available!")

        else:
            for question,answer in flashcards.items():
                print("\n Question:",question)
                input("press Enter to reveal the answer...")
                print("Answer:",answer)

    elif choice=="2":
        question=input("Enter your question:")
        answer=input("Enter the answer:")

        if question and answer:
            flashcards[question]=answer
            print("Flashcard Added sucessfully!")
        else:
            print("Question and answer cannot be empty!")

    elif choice=="3":
        if flashcards:
            for question,answer in flashcards.items():
                print("\n Question:",question)
                print("Answer:",answer)
        else:
            print("No flashcards available!")

    elif choice=="4":
        print("Happy learning!Goodbye.")
        break
    else:
        print("Invalid choice! Try again.")
