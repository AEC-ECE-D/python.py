english=int(input())
telugu=int(input())
hindi=int(input())
maths=int(input())
science=int(input())
social=int(input())
c=0
total=english+telugu+hindi+maths+social+science
per=total//6
print("total marks",total)
print("percentage",per)
if english>=35 and telugu>=35 and hindi>=35 and maths>=35 and science>=35 and social>=35:
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
if english<35:
    c+=1
    print("english fail")
    if telugu<35:
        c+=1
        print("telugu fail")
    if hindi<35:
        print("hindi fail")
        c+=1
    if maths<35:
        print("maths fail")
        c+=1
    if science<35:
        print("science fail")
        c+=1
    if social<35:
        print("social fail")
        c+=1
print("count",c)
def ststus(marks):
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


