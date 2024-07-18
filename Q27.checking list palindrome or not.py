def is_paliy(l):
    reversed_l=l[::-1]
    if l==reversed_l:
        return True
    else:
        return False
l=[]
while True:
    a=input("want to enter a number(y/n):")
    if a=="y":
        n=int(input("enter a number:"))
        l.append(n)
    else:
        break   
print(is_paliy(l))     
print(l)

