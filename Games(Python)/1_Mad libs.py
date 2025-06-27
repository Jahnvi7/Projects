V = 10
A = 0

def vi(): # Input Validation Function
    def gi(prompt, max_len=30): #Get Input Function
        while True:
            v = input(prompt).strip()
            if v and len(v) <= max_len:
                return v
            print(f"❗ Input can not be empty or up to {max_len} characters.")

    def ga(prompt): #Get Age Function
        while True:
            try:
                a = int(input(prompt))
                if 1 <= a <= 120:
                    return a
                print("❗ Age must be between 1 and 120.")
            except ValueError:
                print("❗ Please enter a valid number.")
    
    # Collects all inputs
    n = gi("Enter your name: ", 20)
    a = ga("Enter your age: ")
    c = gi("Enter your city: ", 20)
    u = gi("Enter your university: ", 30)
    fc = gi("Enter your favorite color: ", 15)
    fg = gi("Enter your favorite game: ", 20)
    ff = gi("Enter your favorite food: ", 20)
    fm = gi("Enter your favorite movie: ", 25)
    d = gi("Enter your dream job: ", 25)

    return n, a, c, u, fc, fg, ff, fm, d

# This loop creates n breaks when done..
while True:
    if A <= V:
        A += 1
    else:
        break

n, a, c, u, fc, fg, ff, fm, d = vi()

#This is a simple Mad Libs game where the user inputs various details about themselves.
print (                         )
print (                         )
print("Here is your Mad Libs story:")
print("----------------------------")
print("Your name is " + n + ".")
print("You are " + str(a) + " years old.")
print("You live in " + c + ".")
print("You are a student at " + u + ".")
print("Your favorite color is " + fc + ".")
print("You like to play " + fg + ".")
print("Your favorite food is " + ff + ".")
print("Your favorite movie is " + fm + ".")
print("You want to be a " + d + " when you grow up.")
print("----------------------------")
print("Thanks for playing!")