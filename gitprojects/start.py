print("Hey, Welcome to my simple calculator!")


# my simple calculator
def calculator():
    operation = input("Choose an operation (+, -, *, /): ")
    if operation in ('+', '-', '*', '/'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

        if operation == '+':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operation == '-':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operation == '*':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operation == '/':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error! Division by zero.")
    else:
        print("Invalid operation. Please choose from (+, -, *, /).")
        

if __name__ == "__main__":
    calculator()