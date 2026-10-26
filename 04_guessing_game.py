# import random in order to be able to generate a random value
import random 

#assign a random number from 1 and 100 to variable 'number'
number = random.randint(1, 100)

#set initial amount of guesses to 0
guess = 0

# while guess limit not exceeded, execute code below
while(guess <= 7):
    # prompt for user input
    user_input = input("Enter number: ")
    
    # use try and except to check for non-numeric input
    try:
        # convert user input to an int
        u_input = int(user_input)
    except:
        # if user inputs a non-numeric(non-convertable) value, set u_input to -1
        u_input = -1
    
    # since invalid input is -1, all valid inputs are > 0
    if u_input > 0:
        # compare user input to number
        if u_input > number:
            # increment guess by 1
            guess = guess + 1
            # print "Too high" message
            print("Too high")
        # compare again (if lower this time)
        elif u_input < number:
            #increment guess
            guess = guess + 1
            #print "Too low" message
            print("Too low")
        # also check if user input is correct number
        elif u_input == number:
            # increment guess
            guess = guess + 1
            # print correct guess message
            print(f"Correct in {guess} guesses.")
            # break out of loop
            break
    # if guess is invalid(i.e u_input <= 0) (u_input = -1 so this returns true)
    else:
        # increment guess by 1
        guess = guess + 1
        # print error message
        print("Invalid input: Please enter integer values!")
    
    # checks if number of guesses = 7 and 7th guess is wrong 
    if guess == 7:
        # print "Out of guesses" message
        print(f"Out of guesses. Number is {number}")
        # break loop
        break