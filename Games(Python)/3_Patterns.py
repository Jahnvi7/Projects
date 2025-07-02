# pramid pattern
print("Pramid pattern;")
while True:
    try:
        pra = int(input("Enter number: "))
        
        for i in range(1, pra + 1):
            print(" " * (pra - i) + "*" * (2 * i - 1))
        break
    except ValueError:
        print("Invalid input. Please enter number")

# triangle pattern
print("Trinagle pattern;")
while True:
    try:
        tri = int(input("Enter number: "))
        
        for i in range(1, tri + 1):
            print("*" * i)
    except ValueError:
        print("Invalid input. Please enter number")
    else:
        break

# rectangle pattern
print("Rectangle pattern;")
while True:
    try:
        rec = int(input("Enter number: "))
        
        for i in range(1, rec+1):
            if i == 1 or i == rec:
                print("*" * rec)  # Full row
            else:
                print("*" + " " * (rec - 2) + "*")  # Hollow middle rows
        print("")
    except ValueError:
        print("Invalid input. Please enter number")
    else:
        break