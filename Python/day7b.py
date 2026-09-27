# #9. Functions
# def func():
#     print("Hello World!")
# func()

# #Indentation
# #The spaces at the beginning of a line are called indentation. In Python, indentation is used to define the blocks of code. 
# # For example, in a function, the code inside the function is indented. Also, in loops and conditional statements, the code 
# # inside the loop or conditional statement is indented.


# #10. Function with parameters
# def greet(name): #name is parameter of the function greet
#     print(f"Hello, {name}!")
# greet("Alice")  #Alice is argument passed to the function greet
# greet("Bob")    #Bob is argument passed to the function greet


# #11. Function with return value
# def add(a, b):
#     print(a + b)
# add(5, 10) #returns 15

# bus = 500
# food = 1500
# def expenses(bus, food):
#     print(f"{bus+food}") 
# expenses(500, 1500)


# #return vs print
# def add(a, b):
#     print(a+b)
# add(5,10)

def add2(a, b):
    return a+b
result = add2(5, 10)
print(result)