class Student:
    def __init__(self):
        self.name="divya"
        self.rollno=9
        self.marks=98
    def talk(self):
        print("hello my name is:",self.name)
        print("my rollno is:",self.rollno)
        print("my marks is:",self.marks)
s1=Student()
s1.talk()