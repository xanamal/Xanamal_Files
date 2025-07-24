import math

def is_perfect_square(n): # Check if n is a perfect square
    sqrt_n = math.isqrt(n)  # integer square root
    return sqrt_n * sqrt_n == n # Check if the square of the integer square root equals n

def get_factors(n): # Get all factors of n
    factors = []
    for i in range(1, n + 1): # Loop from 1 to n
        if n % i == 0:
            factors.append(i)
    return factors

# Main program loop
while True: # Start an infinite loop to allow multiple entries
    number = int(input("Enter a whole number: ")) # Prompt user for a whole number

    print(f"\nThe number you entered is {number}.") # Display the entered number

    # Even or odd
    if number % 2 == 0: # Check if the number is even or odd
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

    # Perfect square check
    if is_perfect_square(number): # Check if the number is a perfect square
        print(f"{number} has a perfect square root: {math.isqrt(number)}.")
    else:
        print(f"{number} does not have a perfect square root.")

    # Factors
    factors = get_factors(number) # Get all factors of the number
    print(f"The factors of {number} are {', '.join(map(str, factors))}.")

    # Ask to continue
    choice = input("\nWould you like to enter another number? (Y/N): ") # Prompt user to continue or exit
    if choice.lower() != 'y': # Exit the loop if user does not want to continue
        print("\nThank you for playing!")
        break
