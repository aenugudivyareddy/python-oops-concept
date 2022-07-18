class Test:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
        self.d=40
t1=Test()
t1.m1()
print(t1.a,t1.b,t1.c,t1.d)
print(t1.__dict__)
t2=Test()
t2.c=88
t2.e=99
t2.g=66
print(t2.__dict__)
print(t2.e,t2.g)




