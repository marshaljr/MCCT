# for i in range(1,6):
#     # print(f"{'*' * (i + 1)}")
#     print(f"{'*' * i}")


# for char in "HELLO":
#     print(char)


# word = "HELLO"
# for i in word:
#     print(i)


# i = 0
# while i <= 5:
#     print(i)
#     i += 1

#For loop is used when we know the number of iterations in advance, while loop is used when we don't know the number of iterations in advance.
#While loop is used when we want to repeat a block of code until a certain condition is met.




# entered_password = input("Enter your password: ")

# while entered_password != "1234":
#     print("Incorrect password. Please try again.")
#     entered_password = input("Enter your password: ")
# print("Access granted.")



# input_number = int(input("Enter a number: "))

# while input_number in [1, 2, 3]:
#     if input_number == 1:
#      print("Hello")

#     elif input_number == 2:
#         print("You entered 2.")

#     elif input_number == 3:
#             print("You entered 3.")

#     input_number = int(input("Enter a number: "))

#     print("Invalid input. Please enter 1, 2, or 3.")




# ATM Withdrawal Mechanism

correct_pin = 1234
balance = 50000

pin = int(input("Enter your PIN: "))

# Check PIN
if pin == correct_pin:

    print("PIN is correct.")
    print("Your current balance is:", balance)

    amount = int(input("Enter withdrawal amount: "))

    # Check withdrawal amount
    if amount <= 0:
        print("Invalid amount.")

    elif amount > balance:
        print("Insufficient balance.")

    # elif amount % 500 != 0:
    #     print("Invalid amount. Please enter an amount in multiples of 500.")

    else:
        balance = balance - amount

        print("Withdrawal successful.")
        print("Please collect your cash.")
        print("Remaining balance:", balance)

else:
    print("Invalid PIN.")
    print("Transaction cancelled.")