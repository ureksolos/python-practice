# for-loop implementation of guessing game
import random

number = random.randint(1, 100)
guess = 0

for guess in range(7):
    u_input = input("Enter number: ")
    try:
        u_input_int = int(u_input)
    except:
        u_input_int = -1
    if u_input_int > 0:
        if u_input_int > number:
            guess = guess + 1
            print("Too high")
        elif u_input_int < number:
            guess = guess + 1
            print("Too low")
        else:
            guess = guess + 1
            print(f"Correct in {guess} guesses.")
            break
    else:
        guess = guess + 1
        print("Invalid input: Please enter integer values!")
else:
    print(f"Out of guesses. Number is {number}")
    