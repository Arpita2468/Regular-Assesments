# a=int(input("Enter first term: "))
# d=int(input("Enter Common Difference: "))
# r=int(input("Enter ratio:"))
ap=[1,3,5,7,9,11]
d=ap[1]-ap[0]
for i in range(len(ap)):
    if ap[i] != ap[0]+i*d:
        print("Not AP")
        break
print("AP confirmed")
gp=[1,2,4,8,16,32]
r=gp[-1]/gp[-2]
for i in range(len(gp)):
    if gp[i] != gp[0]*r**i:
        print("Not AP")
        break
print("GP confirmed")
# for i in range(10):
#     print(a+i*d)
# print("______________________________")
# for i in range(10):
#     print(a*r**i)
