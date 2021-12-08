""""
15
1 2 3 2 4 5 6 5 7 6 8 9 8 7 2
9
"""
n=int(input())
data=list(map(int,input().split()))
dic={}

for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
d=-1
for k,v in dic.items():
    if v==1:
        d=k
print(d,end="  ")
