amount = float(input("Enter purchase amount: "))
coupon = input("Do you have a coupon? (yes/no): ").lower()

if amount >= 1000:
    if coupon == "yes":
        print("Discount applied")
    else:
        print("No coupon, no discount")
else:
    print("Minimum purchase of ₹1000 required")