c1s=int(input("enter start position of car 1:"))
c1v=int(input("enter speed of car 1:"))
c2s=int(input("enter the start position of car 2:"))
c2v=int(input("enter the speed of car 2:"))
c=c1s
d=c2s
f=0
while(True):
     c=c1v+c
     d=c2v+d
     if(c==d):
         f=1
         break
if(f==1):
    print("Yes")
else:
    print("No")
        
