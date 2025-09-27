def add_num():
    """
    Adds two given numbers.

    This function prompts the user for two integers, adds them together,
    and prints the result. If the input is not a number, it will keep asking 
    until valid input is provided.

    Raises:
        ValueError: If the user enters a non-integer value.
    
    Returns:
        None
    """
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            result = num1 + num2
            print(f"The result of addition is: {result}")
            break
        except ValueError:
            print("Invalid input! Please enter integers only.")


def div_num():
    """
    Divides two given numbers.

    This function prompts the user for two integers, divides the first by 
    the second, and prints the result. If the input is not a number, it will 
    keep asking until valid input is provided.

    Raises:
        ValueError: If the user enters a non-integer value.
        ZeroDivisionError: If the second number is zero.

    Returns:
        None
    """
    while True:
        try:
            num1 = int(input("Enter the numerator: "))
            num2 = int(input("Enter the denominator: "))
            result = num1 / num2
            print(f"The result of division is: {result}")
            break
        except ValueError:
            print("Invalid input! Please enter integers only.")
        except ZeroDivisionError:
            print("Division by zero is not allowed. Try again.")


