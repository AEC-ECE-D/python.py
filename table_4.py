num1,num2=map(int,input().split())
for i in  range(1,num2+1):
    if num1*i<num2:
        print(num1,"x",i,"=",num1*i)
    else:
         break

