num1,num2=map(int,input().split())
for i in  range(1,num2+1):
    if i%num1==0:
        continue 
    print(num1,"x",i,"=",num1*i)
