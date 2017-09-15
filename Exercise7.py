bill = raw_input("What's the total bill amount? ")
service = raw_input("How was the level of service? Good, Fair, or Bad? ")
Tip = 0
Total = Tip + int(bill)

if service.lower() == "good":
    Tip = .2 * int(bill)
    print("Tip Amount:$ " + str(Tip))
    print("Total Amount:$ " + str(Tip + Total))
elif service.lower() == "fair":
    Tip = .15 * int(bill)
    print("Tip Amount:$ " + str(Tip))
    print("Total Amount:$ " + str(Tip + Total))
elif service.lower() == "bad":
    Tip = .10 * int(bill)
    print("Tip Amount:$ " + str(Tip))
    print("Total Amount:$ " + str(Tip + Total))
else:
    service = raw_input("How was the level of service? Good, Fair, or Bad? ")
