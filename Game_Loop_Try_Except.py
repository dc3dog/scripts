import random
import time

print("I'm thinking of a number...")
time.sleep(2)

# need to include error handling in case letters or 3 digit number is entered
try:
    guess = int(input("Guess a number between 0 and 100: "))
except Exception as e:
    pass

def one_or_two_digit_number(int):
    if len(random.randint) > 2:
        raise Exception("Number must be BETWEEN 0 and 100!")
correct_number = random.randint(1,99)
guess_count = 1

try:
    while guess != correct_number:
        time.sleep(1)
        guess_count += 1
        if guess < correct_number:
            guess = int(input("Incorrect, guess higher: "))
        else:
            guess = int(input("Guess again. Lower this time: "))
except Exception as e:
    pass

#except NumberError:
#    print("Numbers only")
#    print("Enter a number between 0 and 100")

print(f"That's right! The answer is {correct_number}. It took you only {guess_count} guesses!")