class bank:
    def __init__(self,acc_number,acc_holder,balance=0):
        self.acc_number=acc_number
        self.acc_holder=acc_holder
        self.balance=balance
    def deposit_amount(self,d_amount):
        if str(d_amount).isdigit() and d_amount!=0:
            self.balance+=d_amount
            print(f'Rs.{d_amount} deposited Successful')
            print("Current Balance :Rs.",self.balance)
        else:
            print("!!!!!!!! Invalid Amount !!!!!!!!")
    def withdraw_amount(self,w_amount):
        if str(w_amount).isdigit() and w_amount<=self.balance:
            self.balance-=w_amount
            print(f'\nrs.{w_amount} withdraw Successful')
            print("Current Balance :rs.",self.balance)
        elif not(str(w_amount).isdigit()):
            print("\n!!!!!!!! Invalid Amount !!!!!!!!")
        else:
            print("\nInsufficient Balance")
            print("You balance is :",self.balance)
    def acc_detail(self):
        print(f'''
Account Number : {self.acc_number}
Account Holder Name : {self.acc_holder}
Available Balance : Rs.{self.balance}''')

if __name__=='__main__':
    acno=int(input("Enter your Account Number :"))
    acname=input("Enter Your Name :")
    bal=int(input("Enter Initial Amount :"))
    ac1=bank(acno,acname,bal)
    print("             WELCOME TO APNI BANK")
    while True:
        print(f'''      
1.Account Details
2.Deposit Amount
3.Withdraw Amount  
4.Exit
    ''')
        ch=int(input("\nEnter your choice : "))
        if ch==1:
            ac1.acc_detail()
        elif ch==2:
            d_amount=int(input("\nEnter amount to deposit :Rs."))
            ac1.deposit_amount(d_amount)
        elif ch==3:
            w_amount=int(input("\nEnter amount to Withdraw :Rs."))
            ac1.withdraw_amount(w_amount)
        elif ch==4:
            print("\n_________Thank You for visiting_________\n")
            break
        else:
            print("!!!!!!!! Invalid choice !!!!!!!!")
