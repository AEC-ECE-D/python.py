num =input("enter a number :")
sum=0
temp=int(num)
for i in range(len(num)):
    sum=sum+temp%10
    temp=int(temp/10)
print("the sum of digits:::",sum)