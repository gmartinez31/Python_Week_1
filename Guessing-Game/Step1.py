### Step 1 ###
import random
secretnumber = random.randint(1,10)

print("I'm thinking of a number between 1 and 10. Guess it.")
while True:
    guess = input("What's the number?? ")
    guesses = 5 - guess
    print('You have {} guess left.'.format(guesses))
    if guesses == 5:
        print("You ran out of guesses!")
        break

    if guess == secretnumber:
        print("Yes! You got it!")
        break

    else:
        if guess < secretnumber:
            print(str(guess) + " is too low! Try again!")
        else:
            print(str(guess) + " is too high! Try again!")

### Step 2 ###
