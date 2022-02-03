numbers=[2,2,4,6,3,7,8,3,8,9,]
single=[]
for number in numbers:
    if number not in single:
        single.append(number)
print(single)
