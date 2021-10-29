s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
s5=int(input())
s6=int(input())
c=0

total=s1+s2+s3+s4+s6
per=total//6
print(total,per)
if s1>=35 and s2>=35 and s3>=35 and s4>=35 and s5>=35 and s6>=35:
    if per>=75:
        print("dict")
    elif per>=60:
        print("first")
    elif per>=50:
        print("second")
    else:
        print("third")
else:
    print("fail")
if s1<35:
    c+=1
    print("s1 fail")
    if s2<35:
        c+=1
        print("s2 fail")
    if s3<35:
        print("s3 fail")
        c+=1
    if s4<35:
        print("s4 fail")
        c+=1
    if s5<35:
        print("s5 fail")
        c+=1
    if s6<35:
        print("s6 fail")
        c+=1
print("count",c)



    
