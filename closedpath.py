n=int(input())
c=0
while n!=0:
    rem=n%10
    n=n//10
    if rem==0 or rem==4 or rem==6 or rem==9:
        c+=1
    elif rem==8:
        c+=2
        
print(c)        
