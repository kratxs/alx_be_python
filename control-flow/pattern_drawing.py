# Prompt user for pattern size
pattern_size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# # Use a while loop to iterate through each row
while row < pattern_size:

# Use a for loop to print asterisks in each row
    for col in range(pattern_size):
        print("*", end="") # Print without moving to a new line

    print()  # move to the next line after each row
    row += 1  # Increment row counter 

 
