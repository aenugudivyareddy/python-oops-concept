class Test:
    a=10
    def __int__(self):
        self.b=20
t1=Test()
t2=Test()
t2.a+=1
print(t2.a)
print(Test.a)
print(t1.a)
print(t1.__dict__)