#Pyramid Pattern Program
def pattern(n):
      k = 2 * n - 2
      for i in range(0,n):
           for j in range(0,k):
               print(end=" ")
           k = k - 1
           for j in range(0, i+1):
                print("*", end=" ")
           print("&#92r")
 
# Reverse Pyramid Pattern Program
def pattern(n):
      k = 2*n -2
      for i in range(n,-1,-1):
           for j in range(k,0,-1):
                print(end=" ")
           k = k +1
           for j in range(0, i+1):
                print("*", end=" ")
           print("&#92r")
 
 #Right Start Pattern Program
def pattern(n):
      for i in range(0, n):
           for j in range(0, i + 1):
                print("* ", end="")
           print("&#92r")
      for i in range(n, 0 , -1):
          for j in range(0, i + 1):
               print("* ", end="")
          print("&#92r")
 
#Left Start Pattern Program
def pattern(n):
    k = 2 * n - 2
    for i in range(0, n-1):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("&#92r")
    k = -1
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("&#92r")
 
#Hourglass Pattern Program

def pattern(n):
     k = n - 2
     for i in range(n, -1 , -1):
          for j in range(k , 0 , -1):
               print(end=" ")
          k = k + 1    
          for j in range(0, i+1):
               print("* " , end="")
          print("&#92r")
      k = 2 * n -2
      for i in range(0 , n+1):
           for j in range(0 , k):
               print(end="")
           k = k - 1
            for j in range(0, i + 1):
                 print("* ", end="")
            print("&#92r")
 
#Half-Pyramid Pattern Program

def pattern(n):
     for i in range(0,n):
         for j in range(0, i+1):
              print("* " , end="")
         print("&#92r")
 
#Left Half-Pyramid Pattern Program

def pattern(n):
     k = 2 * n - 2
     for i in range(0, n):
          for j in range(0, k):
               print(end=" ")
          k = k - 2
          for j in range(0, i + 1):
              print("* ", end="")
          print("&#92r")
  

#Downward Half-Pyramid Pattern Program

def pattern(n):
      for i in range(n, -1, -1):
           for j in range(0, i + 1):
               print("* ", end="")
           print("&#92r")

#Diamond Shaped Pattern Program

def pattern(n):
     k = 2 * n - 2
     for i in range(0, n):
          for j in range(0 , k):
               print(end=" ")
          k = k - 1
          for j in range(0 , i + 1 ):
               print("* ", end="")
          print("&#92r")
     k = n - 2
     for i in range(n , -1, -1):
          for j in range(k , 0 , -1): 
               print(end=" ")
           k = k + 1
           for j in range(0 , i + 1):
                print("* ", end="")
           print("&#92r")

#Diamond Star Pattern Program

for i in range(5):
    for j in range(5):
        if i + j == 2 or i - j == 2 or i + j == 6 or j - i == 2:
            print("*", end="")
        else:
            print(end=" ")
    print()

#Simple Numbers Program

def pattern(n):
    x = 0
    for i in range(0 , n):
        x += 1 
        for j in range(0, i + 1):
            print(x , end=" ") 
        print("\r") 

#Pascal’s Triangle Program

def pascal(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(function(i, j)," ", end="")
        print()
 
def function(n, k):
    res = 1
    if (k &gt; n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
 
    return res

#Half-Pyramid Pattern With Numbers

def pattern(n):
     for i in range(1, n):
         for j in range(1, i + 1):
             print(j, end= " ")

#Diamond Pattern With Numbers

def pattern(n):
    k = 2 * n - 2
    x = 0
    for i in range(0, n):
        x += 1
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("&#92r")
    k = n - 2
    x = n + 2
    for i in range(n, -1, -1):
        x -= 1
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("&#92r")
 

#Data Science Training
 
def pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
 
        print("&#92r")

#Binary Numbers Pattern Program

def pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print('10', end="")
 
        print("&#92r")
 
#Right Alphabetical Triangle

def pattern(n):
    x = 65
    for i in range(0, n):
        ch = chr(x)
        x += 1
        for j in range(0, i + 1):
            print(ch, end=" ")
        print("&#92r")
 

#Character Pattern Program

def pattern(n):
    k = 2 * n - 2
    x = 65
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            ch = chr(x)
            print(ch, end=" ")
            x += 1
        print("&#92r")

#K Shape Character Program

for i in range(7):
    for j in range(7):
        if j == 0 or i - j == 3 or i + j == 3:
            print("*", end="")
        else:
            print(end=" ")
    print()
#Triangle Character Pattern Program

def pattern(n):
    k = 2 * n - 2
    x = 65
    for i in range(0, n):
        ch = chr(x)
        x += 1
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print(ch, end=" ")
        print("&#92r")
 

#Diamond Shaped Character Pattern Program

def pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        x = 65
        for j in range(0, i + 1):
            ch = chr(x)
            print(ch, end=" ")
            x += 1
        print("&#92r")
    k = n - 2
    x = 65
    for i in range(n, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            ch = chr(x)
            print(ch, end=" ")
            x += 1
        print("&#92r")
 
 
