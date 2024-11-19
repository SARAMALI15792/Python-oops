 # class: It is user defined datatype 
 #      -> enable programmer to make it own datatype
 #      ->used to make larger and real world appliocatio
 
 # Syntax : denote by keyword class (name):
 
 




# Object : these are instance of class 
#      -> we can access this from the class


# The function inside the class is called method not fuctio





# class Atm:
    
    
#     def __init__(self):
#         self.pin=''
#         self.balance=0
#         self.menu()
        
        
#     def menu(self):
#         user_input= input("""
#               Hi how can i help u?
#               1.Press 1 for to create pin.
#               2.Press 2 for to change the pin and check
#               3.Press 3 for to check balance and update
#               4.press 4 for to trasfer money
#               5.Press 5 for to withdraw money
#               6.Press 6 for to exit .
              
#               """)
#         if user_input=='1':
#             self.create_pin()
#             self.menu()
#         elif user_input=='2':
#             self.change_pin()
#             self.menu()
            
#         elif user_input=='3':
#             self.check_balance()
#             self.menu()
#         elif user_input=='4':
#             self.transfer_money()
#             self.menu()
#         elif user_input=='5':
#             self.withdraw_money()
#         else:
#             exit()
            
#     def create_pin(self):
#         user_pin=input("Enter to create pin:")
#         self.pin=user_pin
#         print("Your pin create sucessfully")
        
#         user_balance=int(input("Enter your Balnce:"))
#         self.balance=user_balance
#         print("Your amount of Balance is:",self.balance)
        
#     def change_pin(self):
#         user_pin=input("Enter the old pin:")
#         if user_pin==self.pin:
#             new_pin=input("Enter the New pin:")
#             print("New pin created successfully",new_pin)
#             self.pin=new_pin
#             if self.pin==new_pin:
#                 print("True yes it is:",new_pin)
#             else:
#                 print("Flase")
        
#         else:
#             print("Remember the Old pin First")
            
#     def check_balance(self):
    
#       user_pin=input("Enter your pin to check balance:")  
#       if self.pin==user_pin:
#           print("Your curret Balance is:",self.balance)
#           add_balance=int(input("Enter the balance to add::"))
#           add_balance=add_balance+self.balance
         
#           self.balance=add_balance
#           print("Your New Balance is: ",add_balance)
       
#       else:
#           print("::chal gai yha se yad kr ke a pin::")
#     def transfer_money(self):
#         user_pin=input("Enter the pin:")
#         if self.pin==user_pin:
            
#             Transfer_money=int(input("Enter the amount you want to transfer:"))
#             if Transfer_money<=self.balance:
#              Trasfer_To=input("Enter the Reciver Details:::")
#              Transfer_money=self.balance-Transfer_money
#              self.balance=Transfer_money
#              print("you have Successfully transfer money to: ",Trasfer_To)
#              print("your remaning Balance is:",self.balance)
#             else:
#                 print("sae amount dal bahi")
#         else:
#             print("bahi kia krna cha rha ???")
#     def withdraw_money(self):
#         user_pin=input("Enter the pin:")
#         if self.pin==user_pin:
#             amount=int(input("Enter the amount to withdraw:"))
#             if amount<=self.balance:
#                 amount=self.balance-amount
#                 self.balance=amount
#                 print("you have succesfully withdrwa pkr of :",amount)
#             else:
#                 print(" chal phutt yha se okat dekh apni:")
#         else:
#             print("pin sae tyoe kr bahi")
        
            
      
        
        
# sa=Atm()
        
 
 # golden rule of oops:
 #-> only the obj of class can acccess the member of class or method otherwise no ca access that       
   




# class Fraction:
    
#     def __init__(self,x,y,**saram):
#         self.num=x
#         self.den=y
#         self.multiple=saram
        
#     def __str__(self):
#         return '{}/{}'.format(self.num,self.den)
        
    
#     def __add__(self,other):
#         new_num=self.num*other.den+self.den*other.num
#         new_den=self.den*other.den
#         com={**self.multiple,**other.multiple}
#         return Fraction('{}/{}'.format(new_num,new_den,**com))
        
#     def convert__to__decimal(self):
#         return self.num/self.den
        
    
        
# fr1=Fraction(1,22)    
# fr2=Fraction(1,1)
# fr3=Fraction(1,1)

# print(fr1.convert__to__decimal())
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# class Rectangel:
#     def __init__(self,x,y):
#         self.len=x
#         self.widt=y
        
#     def Area(self):
#         return (self.len*self.widt)
#     def permiter(self):
#         return 2*(self.len+self.widt)
    
#     def display(self):
#         print(f'The len of rec is: {self.len}')
#         print(f'the width of rec is: {self.widt}')
#         print(f'the area of rec is : {self.Area()}')
#         print(f'the paremter of rec is :{self.permiter()}')
    
    
# rec=Rectangel(3,4)
# rec.display()














# class Bankaccount:
#     def __init__(self,Name,Balance,Account_number):
#         self.name=Name
#         self.balance=Balance
#         self.accountNumber=Account_number
        
        
#     def Dep(self):
#         dep=int(input("eter the amout ::"))
#         self.balance=self.balance+dep
        
#         print (f'amout {dep} .new balance is: {self.balance}')
#     def withdraw(self):
#         wit=int(input("eter the amout to withdrw:"))
#         if wit<=self.balance:
#          self.balance-=wit
         
#          print(f'you withdrw:{wit} .new balance:{self.balance}')
#         else:
#             print("isufficet ")
#     def fee(self):
#         f=0.05*self.balance
#         self.balance-=f
#         print( f'your fee ducted is {f} ,new bala:{self.balance}')
#     def display(self):
#         print(f"your name is: {self.name}")
#         print(f"your alace is :{self.balance}")
#         print(f"your accout is:{self.accountNumber}")
        
        
# ar=Bankaccount('saram',12000,1234567)
# ar.display()
# ar.Dep()
# ar.fee()
# ar.withdraw()
# ar.display()





# def sum(x):
#     S=0
#     for i in range(1,x+1):
#         S=(i*(i+1)/2)**2
#         print(S)
        
        
# print(sum(10))













# class Bankaccount:
#     def __init__(self,name,balance,accountnumber):
#         self.Name=name
#         self.Balance=balance
#         self.Account_number=accountnumber
        
#     def dep(self):
#         Dep=int(input("Eter the amout"))
#         self.Balance+=Dep
#         print(f' amout dep {Dep} ad ew alace is {self.Balance}')
#     def withdraw(self):
#         wit=int(input("Eter the amout"))
#         self.Balance-=wit
#         print(f' your amout with drwa {wit} ad ew alace is: {self.Balance}')
        
#     def fee(self):
     
#         f=0.05*self.Balance
#         self.Balance-=f
#         print(f'your fee deucted {f} ad e lace is: {self.Balance}')
        
#     def display(self):
#         print(f"your ame is : {self.Name}")
#         print(f"your alace is : {self.Balance}")
#         print(f"your accout umer is :{self.Account_number}")
        
        
# ac=Bankaccount('saram',12000,1234567)
# ac.display()
# ac.withdraw()
# ac.dep()
# ac.fee()
# ac.display()

# class compution:
    
#     def __init__(self):
        
#         try:
#           self.num1=int(input("Eter the Number:"))
#           self.menu()
          
#         except ValueError:
#             print("Invalid input! Please enter integers only.")
#             self.num1 = None
           
#     def menu(self):
#         user_input= input("""
#               Hi how can i help u?
#               1.Press 1 for to calculate factorial of number.
#               2.Press 2 for to calculate the natural sum.
#               3.Press 3 for to the prime Number
#               4.press 4 for to print table of given
#               5.Press 5 for to  prit division
#               6.Press 6 for to exit .
              
#                """)
#         if user_input=='1':
#             self.factorial()
#             self.menu()
#         elif user_input=='2':
#             self.sum_seq()
#         elif user_input=='3':
#             self.prime()
#             self.menu()
#         elif user_input=='4':
#             self.table()
#             self.menu()
#         elif user_input=='5':
#             self.list_div()
#         elif user_input=='6':
#             self.lidivp()
#     def factorial(self):
#         f=1
#         for i in range(1,self.num1+1):
#             f*=i
#         print("fact of gve numer1 is",f)
#     def sum_seq(self):
#         s=0
#         for i in range(1,self.num1+1):
#             s=i*(i+1)/2
#         print("atural sum of um 1 i s:",s)
#     def prime(self):
       
#         if self.num1<=1:
#             return False
#         else:
#             for i in range(2,self.num1+1):
#                 if self.num1%i==0:
#                     break
               
            
#         print (f'{self.num1} is prime umer')
#     def table(self):
#         # print("Welcome to table section")
#         # print("Table of given numer is :",self.num1)
#         # for i in range(1,21):
        
    
    
#         #  print(self.num1,'x',i,'=',self.num1*i,end=" ")
#         #  print()
#         for self.num1 in range(1,10):
#             print(f"tale of give umer is: {self.num1}")
            
#             for i in range(1,11):
#                 print(f"{self.num1} x {i} = {self.num1 * i}",end=" ")
#                 print()
#             print("-"*14)
#     def list_div(self):
#        l=[i for i in range(1,self.num1+1) if i%2==0]
#        print(l)
        
#     def lidivp(self):
#        w=[i for i in range(2,self.num1+1) if all(i%x!=0 for x in range(2,int(self.num1+1)))]
#        print(f'{w}')
         
                
            
            
      
                
                
    
# com=compution() 



















import random

class Flashcard:
    def __init__(self):
         self.fruit={
             
             "Banana": "yellow", 
             "Strawberries": "pink"
         }
         
    def randm(self):
      
       key, value = random.choice(list(self.fruit.items()))
       user_input=input(f"eter the color of fruit:{key}")
       if user_input==value:
           print(f"correct {key}")
       else:
           print(f"ot correct ,the correct color of fruit i s: {value}")
       
fl=Flashcard()    
fl.randm()   
        
        
       
    
    
    
    
       








