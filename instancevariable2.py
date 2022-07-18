from copyreg import constructor
from operator import methodcaller
from tkinter import Variable


class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
        self.d=40
t1=Test()
t1.a=99
t1.b=98

t1.m1()

t1.c=97  
# (we can also add instance varibles by using object refernce)
print(t1.a,t1.b,t1.c,t1.d)
print(t1.__dict__)



# where we can declare instance variables?
"""
inside constructor
inside instance method
outside of the class by using refernce Variable
"""


