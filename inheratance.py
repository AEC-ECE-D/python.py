class student:
    college="AEC"
    def __init__(self,name,age,section):
        self.name = name
        self.age = age
        self.section = section
    def display(self):
        print(self.name,self.age,self.section)
s1=student("vivek",20,"A")
print(s1.college)
s1.display()
