>>> type(data)
<class 'list'>
>>> data=()
>>> type(data)
<class 'tuple'>
>>> st=set()
>>> type(st)
<class 'set'>
>>> d={}
>>> type(d)
<class 'dict'>
>>> data=[]
>>> data=[1234,"vivek",45.879,True]
>>> data
[1234, 'vivek', 45.879, True]
>>> type(data)
<class 'list'>
>>> data=[10,20,30,40,50,60,70,80,90]
>>> data
[10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> data[2]
30
>>> data[-1]
90
>>> len(data)
>>> data[len(data)-1]>>> data[::-1]>>> len(data)
9>>> data.index(40)
5
>>> data.sort()
>>> data
[10, 20, 40, 70, 80, 200]
>>> max(data)
90
>>> min(data)
10
>>> sum(data)
450
[90, 80, 70, 60, 50, 40, 30, 20, 10]
>>> data[::]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
90
>>> data[-1]
90
>>> data[-len(data)]
10
>>> data[2:6]
[30, 40, 50, 60]
>>> data[2:6:1]
[30, 40, 50, 60]
>>> data[2:6:2]
[30, 50]
>>> data
[10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> data[6:2]
[]
>>> data[6:2:-1]
[70, 60, 50, 40]
>>> data[-5:-3]
[50, 60]
>>> data[1:-1]
[20, 30, 40, 50, 60, 70, 80]
>>> data[-1:1]
[]
>>> data[::-1]
[90, 80, 70, 60, 50, 40, 30, 20, 10]
>>> data[::]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> data[2:]
[30, 40, 50, 60, 70, 80, 90]
>>> data[-1:]
[90]
>>> len(data)
9
>>> max(data)
90
>>> min(data)
10
>>> sum(data)
450
>>> type(data)
<class 'list'>
>>> data.append(100) 
>>> data
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
>>> data.insert(2,200)>>> data.index(40)
5
>>> data.sort()
>>> data
[10, 20, 40, 70, 80, 200]
>>> data.reverse()
>>> data
[200, 80, 70, 40, 20, 10]
>>> 10 in data
True
>>> 60 in data
False
>>> 100 not in data
True
>>> 60 not in data
True
>>> data
[10, 20, 200, 30, 40, 50, 60, 70, 80, 90]
>>> a=[1,2,3,4]
>>> b=[5,6,7,8]
>>> a+b
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a
[1, 2, 3, 4]
>>> b
[5, 6, 7, 8]
>>> a.append(b)
>>> len(a)
5
>>> a
[1, 2, 3, 4, [5, 6, 7, 8]]
>>> a
[1, 2, 3, 4, [5, 6, 7, 8]]
>>> a=[1,2,3,4]
>>> a
[1, 2, 3, 4]
>>> b
[5, 6
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> c=a.copy()
>>> c
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> data
[10, 20, 200, 30, 40, 50, 60, 70, 80, 90]
>>> data.pop()
90
>>> , 7, 8]>>> data.pop(3)
30
>>> data
[10, 20, 200, 40, 50, 60, 70, 80]
>>> len(data)
8
>>> data.remove(60)
>>> data
[10, 20, 200, 40, 50, 70, 80]
>>> del data[4]
>>> data
[10, 20, 200, 40, 70, 80]
>>> data.append(40)
>>> data
[10, 20, 200, 40, 70, 80, 40]
>>> data.remove(40)
>>> data
[10, 20, 200, 70, 80, 40]
>>> data.count(40)
1
>>> data.index(40)
5
>>> data.sort()
>>> data
[10, 20, 40, 70, 80, 200]
>>> data.index(40)
5
>>> data.sort()
>>> data
[10, 20, 40, 70, 80, 200]
>>> data.reverse()
>>> data
[200, 80, 70, 40, 20, 10]
>>> 10 in data
True
>>> 60 in data
False
>>> 100 not in data
True
>>> 60 not in data
True
>>> all(a)
True
>>> any(a)
True
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a=[0,0,0]
>>> a
[0, 0, 0]
>>> all(a)
False
>>> any(a)
False
