import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Guess the Number Game!")

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congrats! You guessed the right secret number {secret_number} in {attempts} attempts.")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Thank you for playing!")
