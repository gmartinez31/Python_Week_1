################################################################### 9
for x in range(1,11):
    for y in range(1,11):
        print(str(x) + " X " + str(y) + " = " + str(x*y))

####################### TRIANGLE EXERCISE #########################
#Triangle formula#
#x = n(n+1)/2  where 'x' is the line number and 'n' is the number of dots on 'x'
n = 0
while n < 100:
    n += 1
    formula = str((n * (n+1) / 2))
    print(str(n) + " = triangle number." + formula + " = number of dots. ")
