import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the number guessing game!")
    print("I have chosen a number between 1 and 100. Try to guess what it is!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guess_the_number()

guess_the_number()
