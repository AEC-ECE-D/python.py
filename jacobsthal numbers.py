##jacobsthal series

def jacobsthal(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return jacobsthal(n-1)+2*(jacobsthal(n-2))

n=int(input("enter a number:"))
r=jacobsthal(n)
print(r)
print("the next jacobsthal value is",jacobsthal(n+1))##2**n-jacobsthal(n) 
