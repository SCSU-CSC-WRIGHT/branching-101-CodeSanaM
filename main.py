"""There are 3 errors in this code. Please use your own ability to find them all. Consider this a Python refresher."""

# TE: created a main() function, which calls the calculate_total() function
def main():
    calculate_total()

# TE: placed Sana's existing code into a function
def calculate_total():
    
    total = 0  # Initialize total before using it
    
    for i in range(5):
        number = int(input("Enter a number: "))  # Convert input to integer
        total += number
        
    print("The running total is:",  total) #syntax error

# TE: called main()
main()