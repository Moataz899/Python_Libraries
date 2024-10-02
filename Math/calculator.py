import math 
Operator = input("Enter an Operator (e + - * / ** log  ceil floor gcd trunc sin cos tan log2 sinh cosh tanh %): ")
num1 = float(input("Enter The First Number: "))
num2 = float(input("Enter The Second Number: "))

if Operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif Operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif Operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif Operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
        
elif Operator == "**":
    result = math.pow(num1, num2)
    print(f"{num1} ** {num2} = {result}")
    
elif Operator == "%":
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")

elif Operator == "e":
    result = math.exp(num1)
    print(f"e^({num1}) = {result}")

elif Operator == "log":
    if num1 > 0:
        result = math.log(num1)
        print(f"log({num1}) = {result}")
    else:
        print("Error: Natural logarithm is not defined for negative numbers.")

elif Operator == "ceil":
    result = math.ceil(num1)
    print(f"ceil({num1}) = {result}")

elif Operator == "floor":
    result = math.floor(num1)
    print(f"floor({num1}) = {result}")

elif Operator == "gcd":
    result = math.gcd(int(num1), int(num2))
    print(f"GCD({num1}, {num2}) = {result}")

elif Operator == "sin":
    result = math.sin(math.radians(num1))
    print(f"sin({num1} degrees) = {result}")

elif Operator == "cos":
    result = math.cos(math.radians(num1))
    print(f"cos({num1} degrees) = {result}")

elif Operator == "tan":
    result = math.tan(math.radians(num1))
    print(f"tan({num1} degrees) = {result}")

elif Operator == "trunc":
    result = math.trunc(num1)
    print(f"trunc({num1}) = {result}")

elif Operator == "log2":
    if num1 > 0:
        result = math.log2(num1)
        print(f"log2({num1}) = {result}")
    else:
        print("Error: Base 2 logarithm is not defined for negative numbers.")
        
elif Operator == "sinh":
    result = math.sinh(num1)
    print(f"sinh({num1}) = {result}")

elif Operator == "cosh":
    result = math.cosh(num1)
    print(f"cosh({num1}) = {result}")

elif Operator == "tanh":
    result = math.tanh(num1)
    print(f"tanh({num1}) = {result}")