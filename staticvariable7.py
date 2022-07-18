class Test:
    x=10
    def __init__(self):
        self.y=20
t1=Test()
t2=Test()
t1.x=t1.x+1
t2.y=t2.y+1
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)
print("Test:",Test.x)