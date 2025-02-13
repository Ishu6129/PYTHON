'''
 Method overloading      -->    compile-time Polymorphism
 Firstly python does not supprt method overloading 
 Method overloading means defining multiple methods in same class with same namae but different arguments
'''
#         Given example not work as overloading - it will take those method which is defined later
'''
class asd:
    def add(self, a, b):  # This will not work
        print(a + b)
    
    def add(self, a, b, c):  # This will work
        print(a + b + c)
obj=asd()
obj.add(1,2,3)#6
obj.add(1,2)#error
'''
#     First method for achieving Method overloading
'''
class asd:
    def add(self,a,b,c=0):
        print(a+b+c)
obj=asd()
obj.add(1,2,3)
'''
#     second method for achieving Method overloading
'''
class asd:
    def add(self,*args):  # args = (1,2,3)
        c=0
        for i in args:
            c=c+i
        print(c)
obj=asd()
obj.add(1,2,3)
'''
#       Operator Overloading  --> compile time polymorphism
''' 
class asd:
    def add(self,a,b):
        print(a+b)
    def __add__(self,other):
        print("This is addition")
class sdf(asd):
    def sub(self,a,b):
        print(a-b)
obj1=asd()
obj2=sdf()
obj2+obj1
'''
#               Method Overriding
'''
 Method overriding      -->    Run-time Polymorphism    or    dynamic polymorphism 
 Method overloading means defining same method in child class as defined in parent class 
 In this both method should have same number of arguments 
'''

'''
class asd:
    def add(self,a,b):
        print(a+b)
class sdf(asd):
    def add(self,a,b):
        print(a-b)
obj1=sdf()
obj1.add(1,2)
'''


#                    Abstraction

'''

from abc import ABC,abstractmethod
class c1(ABC):
    @abstractmethod
    def add(self,a,b):
        print(f'{a}+{b} = {a+b}')
    def sub(self,a,b):
        print(a-b)
class c2(c1):
    def add(self,a,b):  # This method is necessary as we use this as abstractmethod in parent class
        super().add(a,b)
    def sub(self,a,b):
        print(f'{a}-{b} = {a-b}')
        
obj=c2()
obj.add(13,12)
obj.sub(13,12)
'''
