class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print("employee number:",self.eno)
        print("employee name:",self.ename)
        print("employee salary:",self.esal)
        print("employee address;",self.eaddr)
e1=Employee(100,"divya",1000,"kmr")
e1.display()
e2=Employee(200,"ravi",2000,"ldp")
e2.display()
