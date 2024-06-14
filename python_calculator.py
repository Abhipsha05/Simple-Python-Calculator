import math

def addition(n1 , n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Cannot divide by zero"

def exponentiation(n1, n2):
    return n1 ** n2

def square_root(n):
    if n >= 0:
        return math.sqrt(n)
    else:
        return "Invalid input for square root"

def modulus(n1, n2):
    if n2 != 0:
        return n1 % n2
    else:
        return "Cannot compute modulus with zero divisor"

print("Select the operation to perform: \n"\
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. Exponentiation\n" \
        "6. Square root\n" \
        "7. Modulus\n")

select = int(input("Select from operations 1-7: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number (0 in case to perform square roots): "))

if select == 1:
    print(num1, "+", num2, "=", addition(num1, num2))
elif select == 2:
    print(num1, "-", num2, "=", subtraction(num1, num2))
elif select == 3:
    print(num1, "*", num2, "=", multiplication(num1, num2))
elif select == 4:
    print(num1, "/", num2, "=", division(num1, num2))
elif select == 5:
    print(num1, "to the power of", num2, "=", exponentiation(num1, num2))
elif select == 6:
    if num2 == 0:
        print("Square root of", num1, "=", square_root(num1))
    else:
        print("Square root operation does not require a second number.")
elif select == 7:
    print(num1, "mod", num2, "=", modulus(num1, num2))
else:
    print("Invalid input")
