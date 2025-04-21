## 🧮 Simple Calculator

This is a simple command-line calculator that lets users perform basic math operations like addition, subtraction, multiplication, and division. It includes input validation and supports continuous use until the user decides to exit.

### 🔧 Features:
- Handles invalid number inputs using `try/except`
- Validates math operator choices
- Prevents division by zero
- Automatically swaps numbers for subtraction to avoid negatives
- User-friendly loop to perform multiple operations

### 💻 Code

```python
while True:
    # Get user input for the first number with error handling
    while True:
        try:
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # Get user input for the second number with error handling
    while True:
        try:
            num2 = int(input("Enter another number: "))
            break
        except ValueError:
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
            if num1 < num2:
                num1, num2 = num2, num1
            subtraction = num1 - num2
            print(f"The subtraction of {num1} and {num2} is {subtraction}")

        case 'x':
            multiply = num1 * num2
            print(f"The multiplication of {num1} and {num2} is {multiply}")

        case '/':
            while True:
                if num2 <= 0:
                    try:
                        num2 = int(input("Enter a number greater than 0: "))
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    break
            division = num1 / num2
            print(f"The division between {num1} and {num2} is {division:.2f}")

        case _:
            print("Input a valid operator")

    check_again = input("Do you wish to perform another operation? (y/n): ").lower().strip()

    if check_again[0] == 'n':
        print("Goodbye, it was lovely having you here.")
        break
```
