import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

# Maximum number of attempts
max_attempts = 5

# Counter for user attempts
attempt_count = 0

while attempt_count < max_attempts:

    try:
        guess = int(
            input("Enter a number between 1 and 20: ")
        )

    except ValueError:
        print("Please enter a valid number.")
        continue

    attempt_count += 1
    remaining_attempts = max_attempts - attempt_count

    # User guessed a larger number
    if guess > secret_number and attempt_count != max_attempts:

        print(
            f"Try a smaller number. "
            f"{remaining_attempts} attempt(s) remaining."
        )

    # User guessed a smaller number
    elif guess < secret_number and attempt_count != max_attempts:

        print(
            f"Try a larger number. "
            f"{remaining_attempts} attempt(s) remaining."
        )

    # Last attempt and still incorrect
    elif guess != secret_number and attempt_count == max_attempts:

        print("You have used all your attempts.")
        break

    # Correct guess
    else:

        print(
            f"Congratulations! "
            f"You guessed correctly. "
            f"The number was {secret_number}."
        )
        break

# User failed to guess the number
if guess != secret_number:

    print("You lost.")
    print(f"The correct number was {secret_number}.")