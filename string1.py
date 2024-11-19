        ##########REMEMBERM the original string cannot be changed it will create anew string to change to apply######

#create string: by (') (" ")(''' ''')  these are used for string for multi comments of text 
#  or we can also access these by s=str()---> which is function to display strings:

# s=str("saram")   <--------
# print(s)
#how to access the specific string ?
#by indexing or postive indexing we can access a specific word as in pyth string are given sequence by pyth we have to access it by
# s="hellow"    <-------
# print(s[4]) <---------  by this method we can access the string words
#or we can use the negative indexing to this : print(s[-1])  <--------
#as the negative index start from -1 to ...  or positve index start from 0 to ....
  
  
  # ------------>>>>>> SLICING -------------->>>>>>>
  #by this we can set a wide range to extract the words from string like
  #print(s[0:5])----->>> set range from index to the last wjich we want to extract:
  # 
# t="hello world saram"
# print(t[0:8])  ---> u can skip the word also like [2: ]or [ :3]
# s="HELLOW WORLD CAMPUSX"
# print(s[::-1])

#  we can reverse the string by : syntax of [::-1] <<<<<< --------

#negaitv eindex me first number must be greater then secomnd
# s=" saram ali"
# print(s[-1:-4:-1]) #it is used to reverse a specific string by format of this 
# print(s[-4:-1])

 #----->>>>OPERATORS ON STRINGS------->>>>
 ##--->> arthametic op used add and multiply +,*
 # 
# print("saram"+' '+ "ali") 
# print("saram" " "*5)
 #now relational  operators--->>> all work on string in python 
 #if string has character it is true if it is empty then it is false;
# 'saram'or  'ali'
# for i in 'saram':   #aslo used on loops:
#   print("ali")
 #now membership operator: which is denoted by "in" exmp:
# 'S' in 'saram'
#other functions of string and all is 
# len ---> len("count character")
#min---->min("count min character ")
#max---->max("count max character instring")
#sorted---->sorted("sort the charcter in list its output is in list:")
# fuction for string are 
# capitalize is used to capital first letter--->"saram".capitalize()

#tile is used to capital first two lwttwer of first word and second word--->"saram ali".title()

#upper is to capitalm all letters---->"hellow world".upper()
#lower is used to small the letters in "SARAM".lower()
#swapcase is used to turn capital into small and small into capital like --->"sAraM Ali".swapcase()


#others function of string are:

# count is used to count how many time a word repaeat the number of charctr repeated like "saram".count('s')
# find is used to identify the position of that chracter or word "saram is sa".find("sa")

#index is same as find but when we do another search in it it will throw error as in find it doesnt throw eroor it throw -1

#other one is endswith("..") and startwith("...") used to check it is start from aspectve character
#name=input(" ")
# name=input(" ")
# gender=input(" ")
# print("hi my name is {} and my gendr is {}".format(name,gender))
   
   
   
   #### this is format function a very popular fuction which we can aslo pass our values to this fucntion used in login page of websites
   
   
   #another string functions are:
   #isalnum() is used to check the string is character or number:
   #isalpha() is used to check the string is cahracter just or another thing:
   #isdigit() is used to check the string it has numbers or not
   #isidentifier is used to check string is identify or used the according to the rule:
# print("saramali".isalpha()) 
# print("abc1234%".isalnum()) 
# print("1234".isdigit())


###########MOST IMPORTANT FUNCTIONS###############
#----------------->>>>>>> SPLIT() IS used to split the whole string or u can pass specfic word to be split:

# print(" my name is saram ali ".split())
# "-".join("saram  ali is coding at advanced lvl:")
# print("saram ali was born in 2005".split("a"))

# print("-".join(["saram", "ali" ,"was", "born", "in", "2005"]))
####################  JOIN() IS USED TO join the word or any other fuction with current string  ##################

###replace("","")it is used to replace a particular string from the whole string 
# print("saram saleem".replace("saleem","ali"))
#last function is strip()is used to remove the spaces from string 
# print("saram           ".strip())

# s=input("enter the email:::")
# print("the user name we extract from email is:",s[0:13])
# s="enter the email::"
# print("charcter  e  repeat::",s.count("e"))
# x=s.index("@")
# print("the username is::",s[0:x])


# s=input("enter the string::")
# word=input("what u search")
# count=0
# for i in s:
#   if i==word:
#     count+=1
# print("fre",count)    
      
      
# s=input("enter the string:")
# remover=input("entert thenword remoe::") 
# result=""
# for i in s:
#   if i !=remover:
#     result=result+i     
# print("remover number is",result)    




# s=(input("enter the string u want to::"))
# flag=True
# for i in range(0,len(s)//2):
#   if s[i] !=s[len(s)-i-1]:  ##used for comparing:::
#     flag=False
#     print("not palindrome:")
#     break
# if flag:
#   print("palindrome:")  


# num=int(input("enter the number:"))
# flag=True
# for i in range(len(num)//2):
#   if num[i]!=num[len(num)-1-i]:
#     flag=False
#     print("not palindrome")
#     break
# if flag:
#   print("pLIN")  
# num = input("Enter the number: ")
# flag = True

# # Check if the number is a palindrome
# for i in range(0,len(num) // 2):
#     if num[i] != num[len(num) - 1 - i]:
#         flag = False
#         print("Not a palindrome")
#         break

# if flag:
#     print("Palindrome")



#as for string palindrome we use ; len to determine

# num=(input("enter:"))
# flag=True
# for i in range(0,len(num)//2):
#   if num[i] !=num[len(num)-1-i]:
#     flag=False
#     print("not palindrome")
#     break
# if flag:
#    print("palid")  

# num=input("enter the number:")
# flag =True
# if num==num[::-1]:
#   print("palindrome")
# else:
#   flag =False
#   print("not palindrome")  
# s=input("enter the spiliting words:")
# new=""
# l=[]
# for i in s:
#   if i!="":
#     new=new+i
#   else:
#     if new:
#      l.append(new)
#      new=""
# if new:
#   l.append(new)
#   print(l)      

# s=input("enter the string:")
# for i in s.split():
#   print(i[0].upper()+i[1:].lower())
# s=input()
# res=' '
# for i in s:
#     res=i+res
    
# print(res)
# s=input()
# rever=" "
# for i in s:
#   rever=i+rever
# print(rever)  


# s=int(input("enter  the number:"))
# digit="012345678"
# new=""
# while s!=0:
#   new=digit[s%10]+new
#   s=s//10
# print(new) 
# print(type(new)) 

# num=int(input("enter:"))
# for i in range(num,0,-1):
#   for j in range(i-1+1,0,-1):
#     print(j,end=" ")
#   print()  


# num=int(input("enter:"))
# for i in range(1,num+1):
#   for j in range(1,i+1):
#     print("*",end=" ")
#   for k in range(num,i,-1):
#     print("*",end=" ")
  
#   print()  
    
    
    
 
# num = int(input("Enter: "))

# # Half triangle
# for i in range(1, num + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     for k in range(num, i, -1):  # This loop handles the reverse triangle on the same line
#         print("*", end=" ")
#     print()  # Move to the next line after each row



# n=int(input("enter the::"))
# for i in range(1,n+1):
#   for j in range(1,i+1):
#     print("*",end=" ")
#   print()
# for k in range(n,0,-1):
#   for s in range(k,0,-1):
#     print("*",end=" ")
#   print()      


# n=int(input("enter the:::"))
# for i in range(1,n+1):
#    for k in range(n-i):
#      print("",end="")
#    for j in range(i+1):
#       print("",end=" ")
      
#    print()   
# n = 3  # Number of rows

# for i in range(n):
#     # Print leading spaces
#     for k in range(n - i - 1):
#         print(" ", end=" ")
    
#     # Print stars
#     for j in range(2 * i + 1):
#         print("*", end=" ")
    
#     print()  # Move to the next line after each row



# Step 1: Input the number of rows
n = int(input("Enter the number of rows: "))

# Step 2: Loop through each row
for i in range(1, n + 1):
    # Step 3: Print leading spaces
    for k in range(n -3):
        print("  ", end="   ")  # Adjust spaces for centering
    
    # Step 4: Print stars
    for j in range(i):
        print("*", end="   ")
    
    # Step 5: Move to the next line
    print()
