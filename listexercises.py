#1
alist = [11, 52, 36, 72, 10, 2312, 12, 593, 2903]
print(sum(alist))

#2
print(max(alist))
# prints largest number in list #

#3
print(min(alist))
# prints smallest number in list #

#4
for x in alist:
    if x % 2 == 0:
        print x
# prints all even numbers in list #

#5 and #6
# first I printed all positive numbers then I printed all positive numbers in a separate list #
blist = [-12, -30, -21, 4, 0, 1, 90, 453, 24321, -9283]
clist = []
for x in blist:
    if x >= 0:
        clist.append(x)
print(clist)

#7 multiplying a list
dlist = [1, 2, 3, 4]
elist = [3 * ii for ii in dlist]
print(elist)

#8 multiplying vectors
# one way to do this is by using the enumerate fucntion. look into that.
flist = [2, 4, 5]
glist = [2, 3, 6]
hlist = []

for xx in range(0, len(flist)):
    hlist.append(flist[xx] * glist[xx])
print(hlist)

#9 & #10 Matrix Addition & Matrix Addition II
m1 = [[300, 600], [700, 1400]]
m2 = [[500, 900], [300, 2300]]
m3 = []
for xxx in range(len(m1)):
    m4 = []
    for yyy in range(len(m1[xxx])):
        m4.append(m1[xxx][yyy] + m2[xxx][yyy])
    m3.append(m4)
print(m3)

m5 = [[1, 1], [1, 1]]
m6 = []
for a in range(len(m3)):
    m7 = []
    for b in range(len(m3[a])):
        m7.append(m3[a][b] + m5[a][b])
    m6.append(m7)
print(m6)

#11 De-Dub Exercise
#lists are unhashable and mutable(can change), unlike sets, so we had to first
#
dublist = ["Sorry", 3, 78, "Hello", 3, "Sorry", 42, "Hi"]
dub = set()
dub.update(dublist)
new_dublist = list(dub)
print(new_dublist)
#or
print(list(set(dublist)))

# ### BONUS: MUlTIPLYING MATRICIES code is wrong
# e1 = [[20, 40], [100,300]]
# e2 = [[50, 90], [70, 140]]
# elast = []
#
# for t in range(len(e1)):
#     e3 = []
#     for s in range(len(e1[t])):
#         e3.append(e1[t][s] * e2[t][s] + e1[t][s] * e2[t][s])
#     elast.append(e3)
# print(elast)
#
