class A:
    def __init__(self):
        print("in A")
        self.x = 10

class B(A):
    def __init__ (self):
        print("in B")
        super().__init__()  
        self.y = 20


obj1 = B()
print(obj1.x)