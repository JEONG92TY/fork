def calculator():
    num1 = float(input("enter first number: "))
    operator = input("enter operator (+, -, *, /): ")
    num2 = float(input("enter second number: "))

    if operator == "+":
        print(f"result: {num1 + num2}")
    elif operator == "-":
        print(f"result: {num1 - num2}")
    elif operator == "*":
        print(f"result: {num1 * num2}")
    elif operator == "/":
        print(f"result: {num1 / num2}")
    else:
        print("invalid operator!")

calculator()
