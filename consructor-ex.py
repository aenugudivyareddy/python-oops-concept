class Emloyee:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename
        print("constuctor execution")
    def display(self):
        print("emloyee no:",self.eno)
        print("employee name:",self.ename)
e1=Emloyee(12,"divya")
e2=Emloyee(13,"ravi")
e1.display()
e2.display()

