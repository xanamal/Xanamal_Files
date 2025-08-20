import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number between 1 and 100...")

    # Step 1: Pick a random number
    secret_number = random.randint(1, 100)

    # Step 2: Set attempts counter
    attempts = 0

    # Step 3: Start the game loop
    while True:
        # Get user guess
        guess = input("Please enter you guess: ")

        # Validate input (make sure it's a number)
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess) # Convert input to integer
        attempts += 1 # Increment attempts

        # Step 4: Compare guess with secret number
        if guess < secret_number:
            print("Too low .")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break

# Run the game
number_guessing_game()
