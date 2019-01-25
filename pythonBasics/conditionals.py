

billAmount = int(input("Enter the bill Amount:"))

if billAmount<500:
    discount = billAmount*0.05
    print("Dicount Amount is: ", discount)
else:
    discount = billAmount*0.10
    print("Dicount Amount is: ", discount)

print("Your final amount is: ", billAmount-discount)
