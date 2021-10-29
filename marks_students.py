
def status(marks):
    if marks>=35:
        s="p"
    else:
        s="f"
    return s
def find_grade(marks):
    if marks>=75:
        g="a+"
    elif marks>=60:
        g="a"
    elif marks>=50:
        g="b"
    else:
        if status(marks)=="f":
            g="f"
        else:
            g="c"
    return g
def bl_count(s1,s2,s3,s4,s5,s6):
    c=0
    if status(s1)=="f":
        c+=1
    if status(s2)=="f":
        c+=1
    if status(s3)=="f":
        c+=1
    if status(s4)=="f":
        c+=1
    if status(s5)=="f":
        c+=1
    if status(s6)=="f":
        c+=1
    return c
def sum(s1,s2,s3,s4,s5,s6):
    return s1+s2+s3+s4+s5+s6
def pers(total):
    return total//6
def vaild(s1,s2,s3,s4,s5,s6):
    if(s1>=0 and s1<=100)and(s2>=0 and s2<=100)and(s3>=0 and s3<=100)and(s4>=0 and s4<=100)and(s5>=0 and s5<=100)and(s6>=0 and s6<=100):
        return True
    else:
        return False
s1,s2,s3,s4,s5,s6=map(int,input().split())
if vaild(s1,s2,s3,s4,s5,s6):
    print("english",s1,100,status(s1),find_grade(s1))
    print("telugu",s2,100,status(s2),find_grade(s2))
    print("hindi",s3,100,status(s3),find_grade(s3))
    print("maths",s4,100,status(s4),find_grade(s4))
    print("science",s5,100,status(s5),find_grade(s5))
    print("social",s6,100,status(s6),find_grade(s6))
    bl=bl_count(s1,s2,s3,s4,s5,s6)
    print("black_log",bl)
    print("total marks=",sum(s1,s2,s3,s4,s5,s6))
    total=s1+s2+s3+s4+s5+s6
    per=pers(total)
    print("total_percentage=",pers(total))
    if bl==0:
        print("Grade=",find_grade(per))
    else:
        print("fail")
else:
    print("Invaild scores")
