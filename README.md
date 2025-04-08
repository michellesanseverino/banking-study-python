# Banking Study Python

This is a simple banking system implemented in Python. The program allows users to perform basic banking operations such as depositing money, withdrawing money, and checking their account balance. It also enforces a transaction limit to ensure responsible usage.

## Features

- **Deposit**: Add money to your account.
- **Withdraw**: Withdraw money from your account, subject to:
  - A maximum withdrawal limit of $500 per transaction.
  - A maximum of 3 withdrawals per session.
  - Sufficient account balance.
- **Check Balance**: View your current account balance and transaction history.
- **Exit**: Exit the program.

## How to Use

1. Run the `banking.py` script in a Python environment.
2. Follow the on-screen instructions to choose an option:
   - `[D] Deposit`
   - `[W] Withdraw`
   - `[B] Balance`
   - `[E] Exit`
3. Enter the required details when prompted (e.g., deposit or withdrawal amount).
4. The program will continue running until you choose the `Exit` option.

## Example

```plaintext
Welcome to the Banking System

[D] Deposit
[W] Withdraw
[B] Balance
[E] Exit

=> D
Enter the amount to deposit: 100
Deposited: $100.00

[D] Deposit
[W] Withdraw
[B] Balance
[E] Exit

=> B

============ Extract =============
Current Balance: $100.00

Transaction History:
Deposited: $100.00

===================================


## Project made during Suzano - Python Developer Bootcamp at DIO