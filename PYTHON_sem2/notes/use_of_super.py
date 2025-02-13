class shape:#base calss
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def area(self):
        return self.height*self.width
    def peri(self):
        return 2*self.height+2*self.width
print("Without using super\n")
#Without using super
    
class rec(shape):#derived class
    def __init_(self,height,width):
        shape.__init__(self,height,width)
class sqr(shape):#derived class
    def __init__(self,width):
        shape.__init__(self,width,width)
print(rec(11,12).area())
print(rec(11,12).peri())
print(sqr(11).area())
print(sqr(11).peri())
print("USING SUPER\n ") 

# USING SUPER    
class rec(shape):#derived class
    def __init_(self,height,width):
        super().__init__(height,width)
class sqr(shape):#derived class
    def __init__(self,width):
        super().__init__(width,width)
        
print(rec(11,12).area())
print(rec(11,12).peri())
print(sqr(11,).area())
print(sqr(11).peri())

print("Constructor overwritting\n")

#Constructor overwritting

class rec(shape):#derived class
    def __init_(self,height,width):
        self.height=height
        self.width=width
class sqr(shape):#derived class
    def __init__(self,width):
        self.height=width
        self.width=width
print(rec(11,12).area())
print(rec(11,12).peri())
print(sqr(11,).area())
print(sqr(11).peri())
