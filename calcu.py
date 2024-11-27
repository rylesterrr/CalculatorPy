num1 = int(input("Enter a number: "))
num2 = int(input("Enter a Second number: "))
opperation = input("+,-,*, / : ")

if opperation == "+":
    result = num1 + num2
    print(f"Total is: {result}")
elif opperation == "-":
    result = num1 - num2
    print(f"Total is: {result}")
elif opperation == "*":
    result = num1 * num2
    print(f"Total is: {result}")
elif opperation == "/":
    result = num1 / num2
    print(f"Total is: {result}")
