class SE:
    def __init__(self,name,age,tech):
        self.name=name
        self.age=age
        self.tech=tech
s1=SE("divya",23,"cse")
s2=SE("ravi",32,"ece")
s1.child="pinky"
s1.child1="vineel"
s2.root="rc"
s2.root1="kfc"
print(s1.__dict__)
print(s2.__dict__)
print(hex(id(s1)))
print(oct(id(s1)))