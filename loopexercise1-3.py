for x in range(1,11):
    print x
for z in range(1,10, 2):
    print z

print("Alright your turn. ")

start = int(input("Which number would you like to start on? "))
finish = int(input("Okay, which number would you like to finish on? "))
onemore = finish + 1
for y in range(start, onemore):
    print y
