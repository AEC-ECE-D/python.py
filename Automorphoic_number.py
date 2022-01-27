num = int(input())  
num_of_digits = len(str(num))  
square = num**2  
last_digits = square%pow(10,num_of_digits)  
if last_digits == num:  
  print("Automorphic Number")  
else:  
  print("Not an Automorphic Number")  
"""
5^2=25 ///last digit 5
25^2=625  /// last digit 12
"""
