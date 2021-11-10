def fact(a):
    count=1
    for i in range(a,0,-1):
        count=count*i
    print(count)
a=int(input())
fact(a)
