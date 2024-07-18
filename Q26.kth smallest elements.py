l=[]
while True:
    a=input("want to enter a number(y/n):")
    if a=="y":
        n=int(input("enter a number:"))
        l.append(n)
    else:
        break        
print(l)
k=int(input("enter the no of index of the element:"))
print(l[k-1])


