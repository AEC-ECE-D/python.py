num = int(input("enter a number:"))
sqr = num*num 
sumOfDigit = 0
while sqr>0:
    sumOfDigit =sumOfDigit + sqr%10
    sqr = sqr//10
if (num == sumOfDigit):
    print("Neon Number")
else:
    print("Not Neon Number")
