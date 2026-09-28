# # mark = int(input("Enter your mark: "))
# # if mark > 40:
# #     print("You have passed the exam.")
# # else:
# #     print("You have failed the exam.")


# #laptop_login = input user
# #pin/fingerprint == login success
# #else login failed

# user = int(input("Enter your user ID: "))
# if user == 1234:
#     pin = int(input("Enter your pin: "))
#     if pin == 5678:
#         print("Login successful.")
#     else:
#         print("Login failed. Incorrect pin.")
# else:
#     print("Login failed. Incorrect user ID.")   



# #ask user for payment wallet
# #if payment made via khalti/esewa

# payment_method = input("Enter your payment method (khalti/esewa): ").lower()

# if payment_method == "khalti" or payment_method == "esewa":
#     print("Payment successful.")
# else:
#     print("Payment failed. Please use khalti or esewa.")    



#need atleast 75% attendance and fees paid to sit for the exam

attendance = int(input("Enter your attendance percentage: "))
fees_paid = input("Have you paid your fees? (yes/no): ").lower()

if attendance >= 75 and fees_paid == "yes":
    print("You are eligible to sit for the exam.")
else:
    print("You are not eligible to sit for the exam.")