################################################################ 4
fives = "*****"
for x in fives:
    print x * 5

################################################################ 5
squaresize = int(input("Using one number, how big do you want the square to be? "))

for y in range(squaresize):
    print("*" * squaresize)

################################################################ 6
width = int(input("Width, bruh? "))
height = int(input("Height, bruh? "))
space = width - 2
blanks = space * " "

print(width * "*")
for z in range(height - 2):
    print("*" + blanks + "*")
print(width * "*")

################################################################ 7
xr = 5

for xy in range(0,xr):
    spaces = xr - xy - 1
    stars = xy * 2 + 1
    print(' ' * spaces + '*' * stars)

################################################################ 8
height2 = int(input("Give me a height for the triangle. "))
for zyx in range(0, height2):
    whitespace = height2 - zyx - 1
    estrellas = zyx * 2 + 1
    print(" " * whitespace + "*" * estrellas)
