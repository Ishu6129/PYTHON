"""
class Employee:
    def detail(self,name,ID,position,salary):
        self.name=name
        self.ID=ID
        self.position=position
        self.salary=salary
    def display(self):
        print(f'''
Name:{self.name}
ID:{self.ID}
Position:{self.position}
Salary:{self.salary}''')
    def update(self,up_salary):
        cl.salary=up_salary
cl=Employee()
cl.detail("Ishu",101,"Manager",100000)
cl.display()
up_salary=int(input("Enter salary to be updated : "))
cl.update(up_salary)
cl.display()
"""
class car:
    def __init__(self,maker,name,model,year,price):
        self.maker=maker
        self.name=name
        self.model=model
        self.price=price
        self.year=year
        self.available=True
    def display_car(self):
        return(f'''      Maker : {self.maker}
       Name : {self.name}
       Model : {self.model}
       Price : {self.price}
       Year : {self.year}
''')
class dealership:
    def __init__(self,dealer_name):
        self.dealer_name=dealer_name
        self.inventory=[]
    def add_to_inventory(self,car):
        self.inventory.append(car)
    def display_available(self):
        count=1
        print(self.dealer_name.center(25," "),"\n")
        for car in self.inventory:
            if car.available:
                print(count,end="")
                print(car.display_car())
                count+=1
    def sell_car(self,customer,index):
        if 0<index<=len(self.inventory) and self.inventory[index-1].available:
            customer.purchase(self.inventory[index-1])
            return self.inventory[index-1]
        
class customer:
    def __init__(self,cname):
        self.cname=cname
        self.purchased_car=[]
    def purchase(self,car):
        self.purchased_car.append(car)
        car.available=False
   

car1=car('Honda','Hondacity','S4',2018,1400000)
car2=car('hyundai','Creta','KnightEdition',2023,2200000)
car3=car('Tata','Nano','Zero',2014,114300)
d1=dealership('ABC MOTORS')
d1.add_to_inventory(car1)
d1.add_to_inventory(car2)
d1.add_to_inventory(car3)
d1.display_available()
name=input("Enter customer name : ")
index=int(input(f'Enter the car Index from [1-{len(d1.inventory)}]'))
c1=customer(name)
purchased_car=d1.sell_car(c1,index)
if purchased_car:
    print(f'{c1.cname} purchased car\n{purchased_car.display_car()}')
else:
    print('car not available')















