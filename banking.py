# This is a simple banking system that allows users to deposit, withdraw, and check their balance.
# It also limits the number of transactions to 3.
# The program will keep running until the user chooses to exit.

# Banking System
print("Welcome to the Banking System")

# Display options to the user
# The user can choose to deposit, withdraw, check balance, or exit the program.
# The program will prompt the user for input and perform the requested action.
display = """
[D] Deposit
[W] Withdraw
[B] Balance
[E] Exit

=> """

# Initialize variables
balance = 0
extract = ""
limit = 500
number_of_withdraws = 0
WITHDRAW_LIMIT = 3

while True:
    option = input(display).strip().upper()

    # Deposit option
    if option == "D":
        amount = float(input("Enter the amount to deposit: "))

        if amount > 0:
            balance += amount
            extract += f"Deposited: ${amount:.2f}\n"
            print(f"Deposited: ${amount:.2f}\n")

        else:
            print("Invalid amount. Please enter a positive number.\n")

    # Withdraw option
    elif option == "W":
        amount = float(input("Enter the amount to withdraw: "))

        # Check if the amount exceeds the limit, balance, or withdraw limit
        exceeded_limit = amount > limit
        exceeded_balance = amount > balance
        exceeded_withdraw_limit = number_of_withdraws >= WITHDRAW_LIMIT

        if exceeded_limit:
            print(f"Withdrawal limit exceeded. Maximum withdrawal amount is ${limit:.2f}.\n")
        elif exceeded_balance:
            print(f"Insufficient balance. Your current balance is ${balance:.2f}.\n")
        elif exceeded_withdraw_limit:
            print(f"Withdrawal limit reached. You can only withdraw {WITHDRAW_LIMIT} times.\n")

        # If all checks pass, proceed with the withdrawal     
        elif amount > 0:
            balance -= amount
            extract += f"Withdrawn: ${amount:.2f}\n"
            number_of_withdraws += 1
            print(f"Withdrawn: ${amount:.2f}\n")

        else:
            print("Invalid amount. Please enter a positive number.\n")

    elif option == "B":
        # Display the balance and transaction history
        print("\n============ Extract =============")   
        print(f"Current Balance: ${balance:.2f}\n")
        print("Transaction History:")   
        print(extract if extract else "No transactions made.\n")
        print("===================================")

    elif option == "E":
        # Exit the program
        print("Thank you for using the Banking System. Goodbye!")
        break

    else:
        # Invalid option
        print("Invalid option. Please choose a valid option.\n")
        
# The program will continue to run until the user chooses to exit.
