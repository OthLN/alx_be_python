def main():
    try:
        size = int(input("Enter the size of the pattern: "))
        for _ in range(size):
            for _ in range(size):
                print("*", end="")
            print()  # Move to the next row
    except ValueError:
        print("Please enter a valid positive integer.")

if __name__ == "__main__":
    main()