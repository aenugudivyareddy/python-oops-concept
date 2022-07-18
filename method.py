class Student:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def display(self):
        print("student name:{},rollno:{},marks:{}".format(self.name,self.rollno,self.marks))
s1=Student("divya",9,76)  
s2=Student("ravi",6,90)
s1.display()
s2.display()     