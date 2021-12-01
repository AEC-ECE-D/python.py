import random
p=[]
k=[]
c=0
for i in range(100):
    p.append(random.randint(0,1))
print(p)
for i in range(99):
    if p[i]==p[i+1] and p[i]==0:
        c+=1
    else:   
        k.append(c)
        c=0
print("the longest run of 0's is ",max(k)+1)        
