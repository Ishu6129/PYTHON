class Munni:
    def __init__(self, name):
        self.rem = name
        self.__rate = "hello"
    
    def __Hide(self):
        print("TBKKK")

    def get(self):
        print(self.rem, self.__rate)
    
    def set(self):
        n = input("Your: ")
        self.__rate = n
        self.__Hide()
        self.get()
        
obj = Munni("Aryan")
print(obj._Munni__rate)
# Object._className__rate:
obj.get()