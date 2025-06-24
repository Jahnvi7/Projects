import random

print("🎯 Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100... Can you guess it?")
print("Choose your difficulty: Easy (10 attempts) or Hard (5 attempts)")

# Difficulty setting
d = input("Enter difficulty (Easy/Hard) : ").strip().lower()
a = 10 if d == "easy" else 5

# Generate the number
sn = random.randint(1, 100)

# Game loop
while a > 0:
    print(f"\nYou have {a} attempts remaining.")
    try:
        g = int(input("Make a guess : "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    if g == sn:
        print(f"🎉 Congrats! You guessed it right. The number was {sn}.")
        break
    elif g < sn:
        print("🔼 Too low!")
    else:
        print("🔽 Too high!")

    a -= 1

    duw = input("Do you want to play again? (yes/no) : ").strip().lower()
    if duw == 'yes':
        sn = random.randint(1, 100)
        a = 10 if d == "easy" else 5
        print("New game started!")
    elif duw == 'no':
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue

# If user fails
if a == 0 and g != sn:
    print(f"\n💀 You've run out of guesses. The number was {sn}. Better luck next time!")

print("🕹️ Game Over")