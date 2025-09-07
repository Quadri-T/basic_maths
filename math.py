def add_num():
    """adds two given numbers"""
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
    """divides two given numbers"""
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 =int(input("Enter second number: " ))
            answer = num1 /num2
            print(f'Your number is {answer} ')
            break
        except ValueError:
            print("Please enter a number")

