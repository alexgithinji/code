while True:
    print("Welcome to the Guess the Number Game!")
    secret_number = 42
    guess = int(input("Guess the secret number (between 1 and 100): "))

    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    elif guess < secret_number:
        print("Try again. Your guess is too low.")
    else:
        print("Try again. Your guess is too high.")







