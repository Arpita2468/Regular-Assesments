l=[]
while True:
    a=input("want to enter a number(y/n):")
    if a=="y":
        n=int(input("enter a number:"))
        f=1
        for i in range(1,n+1):
            f=f*i
        print(f)    
        l.append(f)
    else:
        print(l) 
        break     