# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
i = 0

# Use a while loop to handle rows
while i < size:
    # Use a for loop to print asterisks side by side in each row
    for j in range(size):
        print("*", end="")
    # Print a newline character after each row
    print()
    
    # Increment the counter for the while loop
    i += 1