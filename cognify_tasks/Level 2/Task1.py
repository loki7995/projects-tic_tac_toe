import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low, enter the high number")
    elif guess > secret_number:
        print("Too high, enter the low number")
    else:
        print("Congratulations! You guessed the correct number.")
        break

#OUTPUT
'''Guess the number between 1 and 100
Enter your guess: 45
Too low, enter the high number
Enter your guess: 50
Too low, enter the high number
Enter your guess: 60
Too low, enter the high number
Enter your guess: 70
Too high, enter the low number
Enter your guess: 65
Too low, enter the high number
Enter your guess: 66
Too low, enter the high number
Enter your guess: 67
Too low, enter the high number
Enter your guess: 68
Congratulations! You guessed the correct number.'''    