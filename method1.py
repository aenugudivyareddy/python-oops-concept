from re import X
from tkinter import Y


class Student:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def talk(self):
        print("Student name:{},rollno:{},marks:{}".format(self.name,self.rollno,self.marks))
s1=Student("divya",8,98)
s1.talk()