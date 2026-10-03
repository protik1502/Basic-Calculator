num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the desired operation(+,-,*,%,/,**):")
if operation == "+":
    result = num1 + num2
    print("Answer: ",result)
elif operation == "-":
    result = num1 - num2
    print("Answer: ",result)
elif operation == "*":
    result = num1 * num2
    print("Answer: ",result)
elif operation =="%":
    result = num1 % num2
    print("Answer: ",result)
elif operation =="/":
    result = num1/num2
    print("Answer: ",result)
elif operation == "**":
    result = num1 ** num2
    print("Answer: ",result)
else:
    print("Invalid input so, expected error occured")