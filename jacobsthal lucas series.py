def jacobsthallucas(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return jacobsthallucas(n-1)+2*(jacobsthallucas(n-2))

n=int(input("enter a number:"))
r=jacobsthallucas(n)
print("the jacobsthal-lucas number of",n,"is",r)
print("whereas the next jacobsthal-lucas value is",jacobsthallucas(n+1)) 

