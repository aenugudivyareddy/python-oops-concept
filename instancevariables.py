class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print("Sudent name:",self.name)
        print("Student rollno:",self.rollno)
        print("Student marks:",self.marks)
s1=Student("pinky",3,90)
s1.display()
#print(s1.name,s1.rollno,s1.marks)   (by usng refernce variable we can acess instance variables )
#print(s1.__dict__)    (is used to know the how many instance variables are used inside a class)
