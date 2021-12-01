n=input("enter ur name:")
t=int(input("enter no.of times u want ur name to be printed:"))
if(t>0):
    print((n+"\n")*t)     ##print((n+" ")*t)
else:
    print("printing ur name is not possible")
    print("please try with a valid input")
