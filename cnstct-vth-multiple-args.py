class Student:
    def __init__(self,n='',m=0):
        self.name=n
        self.marks=m
    def display(self):
        print("hi",self.name)
        print("marks",self.marks)
s1=Student()

s1.display()
s2=Student('divya',87)
s2.display()
"""
class Student:
      def __init__(self,n,m):
        self.name=n
        self.marks=m
      def display(self):
        print("hi123",self.name)
        print("marks",self.marks)
s1=Student("divya",98)
s1.display() 
"""