class Test:
    def __init__(self):
        self.b=20
t1=Test()
t2=Test()
t1.a=888
t1.b=999
print(t1.a,t1.b)
print(t1.__dict__)
print(t2.__dict__)