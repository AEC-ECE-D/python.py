n1=int(input())
data1=list(map(int,input().split()))
n2=int(input())
data2=list(map(int,input().split()))
dic={}
for i in data1:
    dic[i]=1
for i in data2:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=0
for j,k in dic.items():
    if k==0:
        print(j,end=' ')
print("  ")
if i in dic and max(data1):
    print("the maximum number in data 1 is:",max(data1))
    if i in dic and max(data2):
        print("the maximum number in data 2 is:",max(data2))
if i in dic and min(data1):
    print("the minimum number in data 1 is:",min(data1))
    if i in dic and min(data2):
        print("the minimum number in data 2 is:",min(data2))
    
"""
7
1 2 3 4 5 6 7
9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7   
the maximum number in data 1 is: 7
the maximum number in data 2 is: 9
the minimum number in data 1 is: 1
the minimum number in data 2 is: 1
"""
