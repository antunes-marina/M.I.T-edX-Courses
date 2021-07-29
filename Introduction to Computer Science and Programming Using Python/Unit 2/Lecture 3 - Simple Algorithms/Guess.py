print("Please think of a number between 0 and 100!")
print("Is your secret number 50?")
x = 0
guess = 50
low = 0
high = guess
secret = int(guess)

instruction = input("Enter 'h' to indicate the guess is too high. \nEnter 'l' to indicate the guess is too low. \nEnter 'c' to indicate I guessed correctly.")

while guess <= 100:
    if instruction.lower() == 'h':
        secret = secret / 2
        print(f"Is your secret number {int(secret)}?")
        instruction = input("Enter 'h' to indicate the guess is too high. \nEnter 'l' to indicate the guess is too low. \nEnter 'c' to indicate I guessed correctly.")
    elif instruction.lower() == 'l':
        secret = secrect + (secret / 2)
        print(f"Is your secret number {int(secret)}?")
        instruction = input("Enter 'h' to indicate the guess is too high. \nEnter 'l' to indicate the guess is too low. \nEnter 'c' to indicate I guessed correctly.")
    elif instruction.lower() == 'c':
        print(f"Game over. Your secret number was: {int(secret)}")
    else:
        print("Sorry, I did not understand your input.")
        print(f"Is your secret number {int(secret)}?")
        instruction = input("Enter 'h' to indicate the guess is too high. \nEnter 'l' to indicate the guess is too low. \nEnter 'c' to indicate I guessed correctly.")
