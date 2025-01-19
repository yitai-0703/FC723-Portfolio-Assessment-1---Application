def gcd(a, b):
    # Base case: if 'a' is 0, the GCD is 'b'
    if a == 0:
        return b
    # Base case: if 'b' is 0, the GCD is 'a'
    if b == 0:
        return a
    # Recursive case: compute the GCD of 'b' and the remainder of 'a' divided by 'b'
    r = a % b
    return gcd(b, r)

def run():
    try:
        # Prompt the user for the first number
        num1 = eval(input("please input first number:"))
        # Prompt the user for the second number
        num2 = eval(input("please input second number:"))
        # Check if both numbers are positive integers
        if num1 <= 0 or num2 <= 0:
            print("please input positive integer")
        else:
            # Compute the GCD using the gcd function
            result = gcd(num1, num2)
            # Output the result to the user
            print(f"The Greatest Common Divisor of {num1} and {num2} is {result}. ")
    except:
        # Handle any exceptions (e.g., invalid input)
        print("invalid value, please input valid number")


if __name__ == "__main__":
    run()