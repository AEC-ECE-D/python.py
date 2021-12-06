def sum_digits(temp):
    sum=0
    for i in range(len(num)):
        sum=sum+temp%10
        temp=int(temp/10)
    return sum
num=input("enter a number::")
temp=int(num)
sum=sum_digits(temp)
print("the sum of digits:",sum)