class Bankacc:
   def __init__(self,accnumber,accname,acctype,accbalance):
       self.accnumber=accnumber
       self.accname=accname
       self.acctype=acctype
       self.accbalance=accbalance
   def deposit(self,amount):
      if(amount>0):
        self.accbalance=self.accbalance+amount
        print("Successfully deposited-",amount)
        print("New balance=",self.accbalance)
      else:
          print("Invalid")
   def withdraw(self,amount):
      if(0<amount<self.accbalance):
         self.accbalance=self.accbalance-amount
      elif(amount>self.accbalance):
         print("not possible")
      else:
         print("Invalid")
   def getbalance(self):
       print("Current balance=",self.accbalance)
acc1=Bankacc("123","abc","savings",10000)  
while True:
  print(""" 1.Deposit 
  2.Withdraw
  3.Balance
  4.Exit""")
  ch=int(input("Enter the choice:"))
  if(ch==1):
     damount=int(input("Enter the amount to be deposited:"))
     acc1.deposit(damount)
  elif(ch==2):
     wamount=int(input("Enter the amount to withdraw:")) 
     acc1.withdraw(wamount)
  elif(ch==3):
      account1.getbalance()
  elif(ch==4):
      exit(0)
  else:
     print("wrong choice")                      
