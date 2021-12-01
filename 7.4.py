n=[]
def is_sorted(n):
    f=0
    for i in range(len(n)-1):
        if(n[i]<n[i+1]):
            f+=1
    if(f==(len(n)-1)):
        print("True")
    else:
        print("False")
k=int(input("enter the range:"))
for i in range(k):
    ele=int(input())
    n.append(ele)
is_sorted(n)   

