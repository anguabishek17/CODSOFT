print("Simple Calculator")
print("Operations: +  -  *  /")

try:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        result = num1 + num2
        print("Result:", result)
    elif op == "-":
        result = num1 - num2
        print("Result:", result)
    elif op == "*":
        result = num1 * num2
        print("Result:", result)
    elif op == "/":
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print("Invalid operator!")

except ValueError:
    print("Invalid input! Please enter numeric values.")
