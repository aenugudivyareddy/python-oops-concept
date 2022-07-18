class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
t1=Test()
t2=Test()
print(t1.__dict__)
print(t2.__dict__)
del t1.c
del t2.c
print('t1:',t1. __dict__)
print('t2:',t2.__dict__)
print(t1.c)

