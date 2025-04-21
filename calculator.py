# 🧮 Simple Calculator with Input Validation and Operator Handling

while True:
    # Get user input for the first number with error handling
    while True:
        try:
            num1 = int(input("Enter a number: "))  # Try converting the input to an integer
            break  # Break if conversion is successful
        except ValueError:  # If user enters something other than a number
            print("Please enter a valid number.")

    # Get user input for the second number with error handling
    while True:
        try:
            num2 = int(input("Enter another number: "))  # Try converting the input to an integer
            break  # Break if conversion is successful
        except ValueError:  # If user enters something other than a number
            print("Please enter a valid number.")

    # Define valid operators
    valid_operator = ['+', '-', 'x', '/']

    # Ask user to choose an operator
    operator = input("Choose an operator ('+', '-', 'x', '/') to perform an operation on the two numbers you inputted: ")

    # Validate the operator input
    while True:
        if operator not in valid_operator:
            operator = input("Choose a valid operator ('+', '-', 'x', '/') to perform an operation on the two numbers you inputted: ")
        else:
            break

    # Use match-case to perform the appropriate operation
    match operator:
        case '+':
            sum = num1 + num2
            print(f"The sum of {num1} and {num2} is {sum}")

        case '-':
            # Swap numbers if needed to avoid negative results
            if num1 < num2:
                num1, num2 = num2, num1
            subtraction = num1 - num2
            print(f"The subtraction of {num1} and {num2} is {subtraction}")

        case 'x':
            multiply = num1 * num2
            print(f"The multiplication of {num1} and {num2} is {multiply}")

        case '/':
            # Ensure second number is not zero or less before dividing
            while True:
                if num2 <= 0:
                    num2 = int(input("Enter a number greater than 0: "))
                else:
                    break
            division = num1 / num2
            print(f"The division between {num1} and {num2} is {division:.2f}")

        case _:
            # Fallback for unknown operator
            print("Input a valid operator")

    # Ask the user if they want to do another calculation
    check_again = input("Do you wish to perform another operation? (y/n): ").lower().strip()

    if check_again[0] == 'n':
        print("Goodbye, it was lovely having you here.")
        break
