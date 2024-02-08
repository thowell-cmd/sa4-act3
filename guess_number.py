number = 10
print("I'm thinking of a number...")
guess_count = 5

while guess_count > 0:
    guess = input(f"What number am I thinking of? {guess_count} guesses left ('q' to quit) ")

    if guess == 'q':
        print(f"The number was {number}.")
        break
    try:
        if int(guess) == number:
            print("Congratulations! You guessed the right number.")
            break
        elif int(guess) < number:
            print('That number is too low! Guess again... ')

        elif int(guess) > number:
            print('That number is too high! Guess again... ')
    except ValueError:
        print('Enter a number')
        continue

    
    guess_count -= 1
    if guess_count == 0:
        print(f'No more guesses left! The number I was thinking of was {number}')
    
        
