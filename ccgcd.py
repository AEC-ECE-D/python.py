## euclid's algorithm also can be used
##gcd(a,b%a)  or  gcd(a,b-a)
a=int(input())
b=int(input())

while True:
    if(a>b):
        a=a-b
    elif a==b:
        print("gcd is ",a)
        break
    else:
        a,b=b,a
    

