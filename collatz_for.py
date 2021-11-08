num,r=map(int,input().split())
for i in range(1,r):
    if num==1:
        print(-1)
        break
    if num%2:
        num=num*3+1
    else:
        num=num//2
else:
    print(num)
