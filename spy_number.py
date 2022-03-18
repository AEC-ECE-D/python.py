num = int(input())
temp = num
product = 1;
while(temp != 0):
    product = product * (temp % 10);
    temp = int(temp / 10)
x=product
tot=0
while(num>0):
    dig=num%10
    tot=tot+dig
    num=num//10
y=tot
if x==y:
    print("Spy Number")
else:
    print("Not Spy Number")
