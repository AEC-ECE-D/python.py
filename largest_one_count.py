n=int(input())
data=list(map(int,input().split()))
c=0
count=0
for i in data:
    if i==1:
        c+=1
    else:
        if c>count:
            count=c
        c=0
if c>count:
    count=c
print(count)
