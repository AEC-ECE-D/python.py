n=input("enter number")
a=len(n)
k=a
for i in range(a):
    if k%3==0:
        if k==a:
            print(n[i],end="")
        else:
            print(',',end="")
            print(n[i],end="")
    else:
        print(n[i],end="")
    k+=-1
