try:    
    age=int(input("Age:"))
    print(age)
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("age cannot be zero")    
except ValueError:
    print("Invalid value")

