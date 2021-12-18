l =[]     
n = int(input("Enter the number of elements in the list:"))   
count=0
for i in range(0,n):      
    l.append(input("Enter the item:"))     
print("printing the list items..")      
for i in l:   
    print(i, end = "  ")     
    count=[i]+[1]
print(count)
    