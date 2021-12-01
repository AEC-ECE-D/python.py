n=int(input("enter a value"))
a=0
b=1
c=2
print(a,b,c,end=" ")
for i in range(3,n):
    d=a+b+c
    print(d,end=" ")
    a,b,c=b,c,d
