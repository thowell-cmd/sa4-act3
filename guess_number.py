number = 10
print("I'm thinking of a number...")
guess_count = 5

while guess_count > 0:
    guess = input(f"What number am I thinking of? {guess_count} guesses left ('q' to quit) ")

    if guess == 'q':
        print(f"The number was {number}.")
        break
    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        guess_count -= 1
        if guess_count > 0:
            print(f"Sorry! That's not quite right. Try again...")
        else:
            print(f'No more guesses left! The number I was thinking of was {number}')
            break