def add_num():
     """
    Divides two given numbers.

    This function prompts the user for two integers, divides the first
    by the second, and prints the result. If the input is not a number,
    it will keep asking until valid input is provided.

    :raises ValueError: If the user enters a non-integer value.
    :raises ZeroDivisionError: If the second number is zero.
    :return: None
    """
     while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 =int(input("Enter second number: " ))
            answer = num1 + num2
            print(f'Your number is {answer}')
            break
        except ValueError:
            print("Please enter a number")

def div_nums():
     """
    Divides two given numbers.

    This function prompts the user for two integers, divides the first
    by the second, and prints the result. If the input is not a number,
    it will keep asking until valid input is provided.

    :raises ValueError: If the user enters a non-integer value.
    :raises ZeroDivisionError: If the second number is zero.
    :return: None
    """
     while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 =int(input("Enter second number: " ))
            answer = num1 /num2
            print(f'Your number is {answer} ')
            break
        except ValueError:
            print("Please enter a number")

