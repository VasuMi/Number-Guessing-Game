import random

print("===================================")
print("  Welcome to Number Guessing Game!")
print("===================================")

print("\nRules:")
print("1. I will think of a number between 1 and 100.")
print("2. You have limited chances to guess the number.")
print("3. I will tell you if your guess is too high or too low.")
print("4. Guess the number correctly to win!")

# Generate random number
number = random.randint(1, 100)

# Difficulty selection
print("\nPlease select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

choice = input("Enter your choice: ")

if choice == "1":
    chances = 10
    difficulty = "Easy"

elif choice == "2":
    chances = 5
    difficulty = "Medium"

elif choice == "3":
    chances = 3
    difficulty = "Hard"

else:
    print("Invalid choice!")
    exit()

print(f"\nGreat! You selected {difficulty} difficulty.")
print("Let's start the game!")

attempts = 0

while attempts < chances:

    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess == number:
        print(f"\n🎉 Congratulations!")
        print(f"You guessed the correct number in {attempts} attempts.")
        break

    elif guess < number:
        print(f"Incorrect! The number is greater than {guess}.")

    else:
        print(f"Incorrect! The number is less than {guess}.")

    remaining = chances - attempts

    if remaining > 0:
        print(f"You have {remaining} chances remaining.")

else:
    print("\n😔 Game Over!")
    print(f"You have used all {chances} chances.")
    print(f"The correct number was {number}.")