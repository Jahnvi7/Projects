import random

def SWG():
    s, w, g = 1, -1, 0
    com = random.choice([s, w, g])  # Computer's choice

    you_val = {"s": s, "w": w, "g": g}
    stat_dict = {s: "Snake", w: "Water", g: "Gun"}

    while True:
        you_dict = input("\nEnter your choice {s, w, g}: ").strip().lower()
        if you_dict in you_val:
            you = you_val[you_dict]
            break
        else:
            print("❌ Invalid input. Please enter only 's', 'w', or 'g'.")

    print(f"You chose {stat_dict[you]}.\nComputer chose {stat_dict[com]}.")

    if com == you:
        print("🤝 It's a draw")
    elif (com == 1 and you == -1) or \
         (com == 0 and you == 1) or \
         (com == -1 and you == 0):
        print("💥 You lose!")
    else:
        print("🎉 You won!")

# Loop to play again
while True:
    SWG()
    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again not in ['yes', 'y']:
        print("👋 Thanks for playing! See you next time.")
        break