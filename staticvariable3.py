class Test:
    a=10
    def __init__(self):
        self.b=20
        Test.c=30
    def m1(self):
        self.d=40
        Test.e=50
t=Test()
t.m1()
print(t.a,t.b,t.c,t.d,t.e)
print(t.a,t.b,t.c)
print(Test.__dict__)