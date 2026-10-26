import random

number = random.randint(1, 100)
guess = 0

while (guess <= 7):
    u_input = input("Enter number: ")
    try:
        user_choice = int(u_input)
    except:
        user_choice = -1

    if user_choice > 0:
        if user_choice > number:
            print("Too high")
            guess = guess + 1
        elif user_choice < number:
            print("Too low")
            guess = guess + 1
        elif user_choice == number:
            guess = guess + 1
            print(f"Correct in {guess} guesses")
            break
    else:
        print("Not a number")
        guess = guess + 1

    if guess == 7:
        print(f"Out of attempts. The number was {number}")
        break