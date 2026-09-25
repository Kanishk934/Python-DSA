balance = 10000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Balance:", balance)

elif choice == 2:
    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance += amount
        print("New balance:", balance)
    else:
        print("Invalid amount")

elif choice == 3:
    amount = float(input("Enter withdrawal amount: "))

    if amount > 0:
        if amount <= balance:
            balance -= amount
            print("New balance:", balance)
        else:
            print("Insufficient balance")
    else:
        print("Invalid amount")

elif choice == 4:
    print("Thank you")

else:
    print("Invalid choice")