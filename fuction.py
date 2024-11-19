# function::::
#----> are used to to compile your progrma with ur name
#----> u can use it many time as u want 
# ---> it has two parts 
#abstraction and decompostion
#abstraction is something which we cannot see as it is present in the program 
#like func when we write the code in func as it execute then we see the output not execution


#decomposition is something are like small parts which make a program 
#like we wannt to make a model we have divided it ito parts like first is headig secod is theme third is user login page..
#all these are sequence are required / joined which is called decomposition


# def full_triangle(w):
#     # Ascending part for full triangle
#     for i in range(1, w + 1):
#         # Print leading spaces for symmetry
#         print(" " * (w - i), end="")
#         # Print numbers in ascending order
#         for j in range(1, i + 1):
#             print(j, end="")
#         print()    
#     #     # Print numbers in descending order
#     # #     for j in range(i - 1, 0, -1):
#     # #         print(j, end="")
#     # #     print()  # Move to the next line after each row

#     # # # Descending part for full triangle
#     # # for i in range(w - 1, 0, -1):
#     # #     # Print leading spaces for symmetry
#     # #     print(" " * (w - i), end="")
#     # #     # Print numbers in ascending order
#     #     for j in range(1, i + 1):
#     #         print(j, end="")
#     #     # Print numbers in descending order
#     #     for j in range(i - 1, 0, -1):
#     #         print(j, end="")
#     #     print()  # Move to the next line after each row


# # Get user input
# x = int(input("Enter the number: "))
# full_triangle(x)

# def loop(x):
#     for i in range(1,x+1):
#         print("   "*(x-i),end="  ")
#         for j in range(1,i+1):
#             print(j,end="  ")
#         print( )    
            
#     for i in range(x-1,0,-1):
#         print("  "*(x-i),end="")
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()
 
 
# w=int(input("enter the number")) 
# print(loop(w))          



# deafult argument is used to when user passed nothing like in parameters
#as it follows the ordders
# def power(a=1,b=1):
    
#     return a+b


# print("welcome to addition of number")

# print(power(12)) # defult argumet
# # we can also use the keyword argument :

# print(power(a=12))

# Original tuple
# t = (1, 5, 7, 8, 10)

# # Create a new tuple with the specified multiplications
# result = (
#     t[0] * t[1],
#     t[0] * t[1] + t[1] * t[2],
#     t[1] * t[2] + t[2] * t[3],
#     t[2] * t[3] + t[3] * t[4],
#     t[3] * t[4]
# )

# print("Resultant tuple after multiplication:", result)

#                                                                                                                                                                                                       t1 = (1,2,3,0)
# t2 = (0,1,2,3)            
# if t1==t2:
#     print("t1 and t2 same")
# el se:
#    print("t1 and t2 are not same") 


# def num(n):..,,,mmmnnnnnnnn
#     d=[]
#     for i in range(n+1):
#         if i%2==0:
#             d.append(i)
#     print(d)
           
            
    
        
# n=int(input("eter the umber")) 
# print(num(n))            







############ very popular fuct which is *args(u can rename the args with ay keyword)

# when we dont know how many times the user pass the values the we use it
# defult it is store in tuple


#like
# def num(*julebahi):
#     """
#      the fuc is used for additon of number
#      created on 12 nov 2024
#      use multiple values user want to print witouh having any limit
#     """
#     a=0
#     for i in julebahi:
#         a=a+i
#     print(julebahi)
#     return a


# print(num(1,2))        
# print(num.__doc__)   # we can also access the doc of the given by this forma567 




##################   **kwargs are used to make a pairs like dict 


# def country(**name):
#     for (key,value) in name.items():
#         print(key,'--->',value)
        
    
# print(country(pakistan='islmabad',nepal='katmdu',india='delhi'))   




# local variable :
# the variale inside the fun is called local varable

# global varaible:
#which is inside the main program are called the global varaible;


# def s(y):
#     y=5
#     y+=1
#     return y


# x=4
# print(s(x))
# print(x)


#nested func :::::::::::


# def f():
#     def c(*sa):
#       w=0

#       for i in sa:
#           w=w+i
         
#       return w
          
#     return c  # it is retur a fuct


# v=f()(2,4,3,3)
# print(v)
      
      
      
      
#pass funtion with funnctio


# def a1():
#     print("you are inside  funct 1")
#     a=[]
#     for i in range(1,10):
#         i%2==0
#         a.append(i)
#     return a  
      
# def b1(z):
#     print("you are inside func 2")
#     return z()
    



# print(b1(a1))
    
    
    
    
    
    
    
#### lamda func is used to code in one line 
# it is anonomous
# canot channge the name of that fuc
#return whole funct
# used to easy the code
# decleared or start with keyword lambda
#syntax of this lambda w:(any logic) w


#example
# a=lambda x:'even' if x%2==0 else 'odd'
# print(a(222))

# a=lambda w:'sa' in w
# print(a("saram"))




# def hof(fun,l):
#     result=[]
#     for i in l:
#         result.append(fun(i))
#     return result    
           
           
           
           
# l=[1,2,3,4] 
# print(hof(lambda x:x**4,l))      
             
             
             
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
######## map is a func whic is used to make a code easier


# t=[1,2,3,4]
# s=tuple(map(lambda x:"even" if x%2==0 else 'odd',t))   
# print(s) 




# we can also fetch a specific something from a dict





# user=[
    
#     {
#       'name':'saram',
#       'age':33,
#       'year':2005,
#     },
#      {
#       'name':'ankit',
#       'age':30,
#       'year':201,
#     },
#      {
#       'name':'rahul',
#       'age':19,
#       'year':2001,
#     },

# ]
      
# x=tuple(map(lambda x:x["year"],user))
# pr
# int(x)
# n=22
# s=tuple(filter(lambda x: n%x==0,map(int,range(1,n+1))))
# print(s)





# def main():
#  while (True):
#      usr=(input("eter the user name"))
#      passw=(input("eter the pass"))
#      """
#      This fuc gett user ad pass from user
#      ad check the pass 
    
#      """
#      if type(usr)==str and type(passw)==str:
#        if usr=='saram' and passw=='saram0987':
#          return 'login Successfull'
#        else:
#          return 'Try again'
#      else:

#         return 'pagal ha kia???'
    
    
 
# print(main())
# print(main().__doc__)



# def lis(s,l):
#  print(s)
#  uique_list=list(set(l))
#  return uique_list


# print(lis(" the uique list is :",[1,2,3,3,3,4,5]))    
    
# def alphbat(hypen):
#  s=hypen.split("-")
#  s.sort()
#  return "-".join(s)
 

# print(alphbat("green-red-yellow-black-white"))    


# def words(s):
#   w=s.count(s.startswith(s.upper))
#   return w
  



# print(words("CampusX is an Online Mentorship Program fOr EnginEering studentS."))
# s="CampusX is an Online Mentorship Program fOr EnginEering studentS."

# w=map(lambda x: x.split(), filter(i for i in x[0:].isupper()), s)



# def letter(s):
 
#     upper=sum(1 for i in s if i.isupper())
#     lower=sum(1 for i in s if i.islower())
#     return upper,lower


# s="CampusX is an Online Mentorship Program fOr EnginEering studentS"
# upper_count ,lower_count=letter(s)
# print("o of upper:",upper_count)
# print("o of lower cout",lower_count)
        
        
        
        
        
# def num(l):
    
#     s=list(filter(lambda x:x%2==0,l))
     
#     return s



# print(num([1,2,3,4,5,6,7,8,9]))


# def is_perfect(n):
#     # Calculate the sum of proper divisors of n
#     divisors_sum = sum(i for i in range(1, n) if n % i == 0)
#     return divisors_sum == n

# # List to store perfect numbers
# perfect_numbers = []

# # Check for perfect numbers in the range from 1 to 10,000
# for n in range(1, 10000):
#     if is_perfect(n):
#         perfect_numbers.append(n)

# # Print the perfect numbers found
# print("Perfect numbers:", perfect_numbers)
# def repeat(stri):
   
#     repeated=stri.lower().count("you")
    
#     return f"you --> {repeated}"

# print(repeat("hello how are you i am fine thank you"))
        


# def d(fun1, fun2, fun3):
#     w = fun1.copy()  # Create a copy of fun1 to avoid modifying the original dictionary
#     w.update(fun2)   # Add the contents of fun2 to w
#     w.update(fun3)   # Add the contents of fun3 to w
#     return w

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}

# print(d(dic1, dic2, dic3))

# import matplotlib.pyplot as plt

# # Sample data
# data = [50, 60, 60, 70, 80, 80, 80, 90, 90, 100]

# # Create a histogram
# plt.hist(data, bins=5, edgecolor='black')

# # Add labels and title
# plt.xlabel('Scores')
# plt.ylabel('Frequency')
# plt.title('Histogram of Exam Scores')

# # Show the plot
# plt.show()














# def cor(l):
#     return min(l,key=lambda l:l[0]**2+l[1]**2)
         
# print(cor([(1,1),(2,2),(3,3),(4,4)]))         




# def add(l1,l2,l3):
#   c=list(lambda l1,l2,l3:map(int,l1+l2,+l3))
#   return c
# print(add([1,2],[3,4],[5,6]))


# def transform_list(input_list):
#     # Use map to raise each element to the power of its index
#     transformed = list(map(lambda x: input_list[x] ** x if x < len(input_list) - 1 else '-', range(len(input_list))))
#     return transformed

# # Example usage
# list1 = [1, 2, 3, 4, 5, 6]
# result = transform_list(list1)

# print(result)







# def vowel(l):
#      v='aeiou'
#      return list(filter(lambda x:x.lower() in v,l))




# print(vowel(['a','e','i','hellow','saram']))

# import functools
# def l(li):
#  return functools.reduce(lambda x:x if ,li)  
# import functools
# def lis(l):
#     return functools.reduce(lambda x,y:x+y,l)


# l=[[1,2],[1,3],[1,5],[1,7]]
# print(lis(l))

# employees = [
#     {
#         'fname':'Nitish',
#         'lname':'Singh',
#         'age' : 33,
#         'grade':'skilled'
#     },
#     {
#         'fname':'Ankit',
#         'lname':'Verma',
#         'age' : 34,
#         'grade':'semi-skilled'
#     },
#     {
#         'fname':'Neha',
#         'lname':'Singh',
#         'age' : 35,
#         'grade':'highly-skilled'
#     },
#     {
#         'fname':'Anurag',
#         'lname':'Kumar',
#         'age' : 30,
#         'grade':'skilled'
#     },
#     {
#         'fname':'Abhinav',
#         'lname':'Sharma',
#         'age' : 37,
#         'grade':'highly-skilled'
#     }
    
# ]
# w=list(map(lambda x:x['fname'] + ' ' + x['lname'],list(filter(lambda x:True if x['grade'] == 'highly-skilled' else False,employees))))
    
# print(w)


# def w(g):
#  return list(map(lambda x:'break'  if x>=3 else 'pass',g ))


# print(w([1,2,3,4,5]))









# def fabonaci(n):
#  a=0
#  v=1
#  sum=0
#  if n==1:
#      return 0
#  else:
#        print(a)
#        print(v)
#        for i in range(1,n+1):
       
#          sum=a+v
#          a=v
#          v=sum
#          print(sum)
    
# print(fabonaci(10))
        
    
from math import factorial   
def pascal(N):
    for i in range(N):
            print(" "*(N-i) ,end=" ")
        
            
            for j in range(i+1):
                ncr=factorial(i)//(factorial(j)*factorial(i-j))
                print(ncr,end="  ")
                
            print("  ")
        
        
s=int(input("enter the number::"))
print(pascal(s))
    
    
    
    
    
    
    
    
