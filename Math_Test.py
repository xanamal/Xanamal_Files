import math

def is_perfect_square(n):
    sqrt_n = math.isqrt(n)  # integer square root
    return sqrt_n * sqrt_n == n

def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# Main program loop
while True:
    number = int(input("Enter a whole number: "))

    print(f"\nThe number you entered is {number}.")

    # Even or odd
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

    # Perfect square check
    if is_perfect_square(number):
        print(f"{number} has a perfect square root: {math.isqrt(number)}.")
    else:
        print(f"{number} does not have a perfect square root.")

    # Factors
    factors = get_factors(number)
    print(f"The factors of {number} are {', '.join(map(str, factors))}.")

    # Ask to continue
    choice = input("\nWould you like to enter another number? (Y/N): ")
    if choice.lower() != 'y':
        print("\nThank you for playing!")
        break
