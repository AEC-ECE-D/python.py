num,r=map(int,input().split())
c=1
while True:
    if c==r:
        print(num)
        break
    if num==1:
        print(-1)
        break
    if num%2:
        num=num*3+1
    else:
        num=num//2
    c+=1
