size = int(input("Enter the size of the pattern: "))
for _ in range(size):
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next row