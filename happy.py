n=int(input("enter the number:"))
sum=0
while sum in range(10):
        rem=n%10
        sum=sum+rem
        n=sum
if sum==1 or sum==7:
     print("happy number")
else:
       print("not a happy number")
    
