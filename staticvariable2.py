class Test:
    a=10
    def __init__(self):
        self.b=20
        Test.c=30
t1=Test()
print(Test.__dict__)

