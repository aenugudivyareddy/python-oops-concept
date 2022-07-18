class Test:
    a=10
    def __init__(self):
        self.b=20
        Test.c=30
    def m1(self):
        self.d=40
        Test.e=50
    @classmethod
    def m2(cls):
        cls.f=60
        Test.g=70
t=Test()
t.m1()
Test.m2()
print(Test.__dict__)
