n=int(input("enter the height of the triangle"))
for i in range(1,n+1):
    if(n>0):
       print("*"*i,end="\n")
else:
     print("Printing the triangle is not possible")
