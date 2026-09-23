#Number conversion 

#Decimal to Binary

num1 = 12345
print(bin(num1))
print(f"{bin(num1)}")

print(hex(num1))
print(f"{hex(num1)}")

print(oct(num1))
print(f"{oct(num1)}")



#Binary to Decimal, Hexadecimal, and Octal

num2 = "11011"
print(f"{int(num2, 2)}")
print(f"{hex(int(num2, 2))}")
print(f"{oct(int(num2, 2))}")



#HexaDecimal to Binary, Decimal, and Octal

num3 = "FAA"
print(f"{bin(int(num3, 16))}")
print(f"{int(num3, 16)}")
print(f"{oct(int(num3, 16))}")



#Take octal numbetr as input and convert in to binary, decimal, and hexa-decimal

num4 = input("Enter an octal number: ")

print(f"{bin(int(num4, 8))}")
print(f"{int(num4, 8)}")
print(f"{hex(int(num4, 8))}")



#Computational Thinking

# --> Optimal Solution / Systematic Solution
# Decomposition: Breaking down a complex problem into smaller, manageable parts.
# Pattern Recognition: Identifying similarities or patterns in the problem to simplify the solution.
# Abstraction: Focusing on the essential details while ignoring irrelevant information.
# Algorithm Design: Creating a step-by-step plan or set of rules to solve the problem efficiently.

#1. Sequential Execution: Executing instructions in a specific order, one after the other.
#2. Conditional Execution: Making decisions based on certain conditions, allowing different paths of execution.
#3. Iterative Execution: Repeating a set of instructions multiple times until a specific condition is met.