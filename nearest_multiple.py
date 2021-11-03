num,r=map(int,input().split())
if r%num==0:
    print(r//num)
else:
    L=r//num
    R=L+1
    if r-L*num==R*num-r:
        print(L,R)
    elif r-L*num>R*num-r:
        print(R)
    else:
        print(L)
