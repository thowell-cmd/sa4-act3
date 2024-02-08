number = 10
print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? ('q' to quit) ")

    if guess == 'q':
        print(f"The number was {number}.")
        break
    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f"Sorry! That's not quite right. Try.")
