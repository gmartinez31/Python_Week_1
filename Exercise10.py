coins = 0
print("You have 0 coins, friend")

while True:
    question = raw_input("Do you want a coin, bub? (yes/no) ")
    if question == "yes":
        coins += 1
        print("You have {} coin(s)").format(coins)

    elif question == "no":
        print("OK. Leave me alone")
        break

    else:
        print("Try again")
