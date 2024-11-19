#list are used when we use multiple items of same datatype thats why we used the list:
   
#------>>>LIST VS ARRAY----->>>>>
#--> ARRAY are fixed when we declare we put the numbers to fixed
#-->LIST is dynamic(means that we can add amny items as we want in that list witout first given the space: )
#-->> array has fixed data types number when we decleare char a[3] it means we just write charcter in it:
#-->> while list has no restriction we can store datatype of any like int,char,string in it or list witin another list.
#speed of list is slower as array is fast in execution
#list occupy more memory as compared to array>
#refrential array ::: is used to store multiple dattypes in array

## dynamic list is increase its size when required in progrm as it is added by one

############CHARACTERISTICS OF LIST############################
# LIST must be in orderded form
#we can change the list/mutable while srting are immutable to change
#hetrogenous(mean we can add different datatypes in list)
#can have duplicate item u can change in program
#dynamic mean it increase its size when required in progrm
#can be accesed using indexing and slicing
#can be nested mean list within another list




##############creating a list##############

#---> 1d list
# print([1,2,3,4]) # homogenous means same
#-->2d list
# print([1,2,3,4,[1,2]]) #hetrogenus mean with differnt datatypes like it has int,list dataype thats why it is hetrogenous:
#-->3d list   it means a list within list a list within list nested list::
# print([[[1,2,3,3],[1,1,1],[1,1,12]]])
# a proper hetrogenous list is:::::
# print([1,3.3,5+5j,'hellow'])
# using type conversion :::: this can used to to convert string into list format like  print(list(write anything u want to convert:))
# print(list("saram ali"))


###############indexing in list##########l
# l=[[[1,2],[2,2],[1,8],[1,1]]]
# print(l[-1][-2][-2])
#first u write the index u want ton extract then u give the another one specifc index to be extract in above example:



##############slicing in list#############
#it is used to extract multiple items from list as in string
# l=[1,2,5,7,9,0,99]
# print(l[-1::-6])
#from this u can jump or extract a specific value of string
# l=[1,2,3,4]
# print(l[::-1])



############APPEND FUNCtion###########
# it is used to append or add oone item in list of any datype 
#like  just one item it add in the list of program
#we can also add the string in list as it support any datype functons
# l=[0,8,3,4,5]
# l.append([2,3,4,5])
# print(l)

###########EXTEND FUNCTION#####################
#it is used to add multiple items in current list
#first it will break the item of any datype then add in the list of program
# l=[1,2,3,4,'saram']
# l.extend([2,2,2,23,4,4])// l.extend('saram') 
# print(l)


#############INSERT FUNC###############
#it is used to add any item at any location in list we use insert func as append and extend func are used to add items at the last of list:
#ex syntax l.insert(1(indexpostionstarty from where and b/w add),100)it meams i want to add 100 b/w 1 and 44

# l=[1,100,3,3,4,5,7,8]
# l.insert(3,99)  ##first is index where we insert and second is number what we insert
# print(l)


###########EDITING A LIST################
# u can edit a list by indexing and slicing
#by slicing i can change mine
# l=[0,9,8,7,6,5]
# l[-4:-1]=[99,88,77]
# print(l)

#by indexing    (when indexing we do not use list bracket while in slicing it is multiple so we used list brackets)
# l=[0,9,8,7,6,5]
# l[3]=100101
# print(l)



##############DELETING ITEMS FROM LIST##################
#del
#remove
#pop
#clear
#these are four function which are used to deleted items from list:
# u can del by indexing and slicing as del l[any number ot thing u want to delte]as by give index or slicing number 
#del
# l=[1,2,3,'saram']
# del l[-3:-1]
# print(l)


#remove it dosesnt require the index it just require the number which want to be remove form list
# l=[1,3,4,6,"saram"]
# l.remove("saram")
# print(l)


#pop is used to delete a item form listb as same in in dele as it defult it delte the last valure when nothing is passed through it
#it i sused by indexing slicing
# l=[1,2,3,4,5,6]
# l.pop(-5)
# print(l)

#clear is used to clear the whole list and included items in that list
# l=[1,2,3]
# l.clear()
# print(l)

############OPERATIONS ON LIST##################
#Arathematic(+,* )
#membership
#


# l=["saram"]
# print(l+l)
# l=["saram",1,2,3,4]
# print(l*3)  #concatenate /mergeing 

##membership
# l=[1,2,3]
# l2=[1,2,3,4,[22,22]]   #### it si false because it is another list as 22 is not seperate in sigle list

# print(22 in l2)  


###looop operators


# l=[[[1,2],[1,1]],[[1,7],[1,9]]]   ###one 2=1 and another 2=1 it act like one item both of two:
# for i in l:
#     print(i)


######MORE FUNC OF LIST###############
#len()
#max
#min
#sorted ()is used to give ascending order and we give descending order by :
# l=[1,5,2,6,2,6]
# l.sort(reverse=True) ## by this we can reverse the list items as by default it gives us ascending order default

# print(l)

#count()is used to count the chracter oritems repeated how many times:
#index() is used to give the position of  of items in list
#reverse ( ) is permanent function which is used to revrse the list as your current list must be finished 
# l=[1,1,2,3,1,3]
# print(l.count(1))


# l=[1,1,2,3,1,3]
# print(l.index(3))

# l=[1,1,2,3,1,3]
# l.reverse()
# print(l)


########### sort vs (sorted)###########
# sort() is used to make a permanent differnce in list 
#while sorted() is used to make a new cell in memory in the list


# l=[1,1,2,3,1,3]
# print(sorted(l))
# print(l)
# l.sort()
# print(l)





#########copy() is used to create a copy of list in memory


# l=[0,3,4,5,6,7]
# print(l)
# l1=l.copy()
# print(id(l))
# print(l1)
# print(id(l1))
# l=[1,2,3,4,5]
# print(l)
# print(id(l))
# l1=l.copy()
# print(l1)
# print(id(l1))
 #first we will create list
 #now print id () of l
 #now create another new variable and equal to now copy()  in it like l1=l.copy()
 
 #now print id (l1) now we see it will give us differnt address in memory
 
 
 ##############LIST COMPRENSHION MOST IMPORTANT ###########
 # synbtax :::::::
 #[expression for expression iterable if condition==true]
#means start expr =i itreable =range



# l=[i for i in range(1,11)]
# print(l) 
    #or it has two methods
# l=[]
# for i in range(1,11):
#     l.append(i)
    
# print(l) 

# s=int(input("enter the "))

# l=[i for i in range(1,s+1) if i%2==0]
# print(l)

 
# v=[1,4,6,7,8]
# s=-4
# l=[s*i for i in v] 
# print(l)



# v=["saram","python",'non','yon']
# l=[v for v in v if v.endswith('n')]
# print(l)


# v=[1,22,333]
# v[-1 ]=3
# l=[num for num in v]
# print(l)

  
# num=(input("enter the :"))
# for i in range(0,len(num)//10):
#     if num==num[::-1]:
#         flag=True
#         print("palindrome:::")
#     else:
#         flag=False
#         print("not palindrome:::")      
 
 
 
 
 
 
 
 #####NESTED LIST COMPREHIONS#####
# fruits=['rahul','ramesh','chohan','ragov']
# fruit=['rahul','kianes','ganesh']
# l=[i for i in fruit if i in fruits if i.startswith("r")]  
# print(l)






# v1=[1,2,3,33]
# v2=[2,22]
# l=[i*j for i in v1 for j in v2]
# print(l)



# l=[[i*j for i in range(1,4)]for j in range(1,4)]
# print(l)




##############TWO TYPES OF WAY TO PRINT LIST ##############

# one is itemwise
#second is index wise

#like example
# l=[]
# for i in range(1,5):
#     l.append(i)
# print(l)      

# l=[1,2,3,4]
# for i in l:
#     print(i)      it is item wise printing now go to index wise printing:

# l=[1,2,3,4]
# for i in range(0,len(l)):
#     print([i])     this is index wise printing of list
     
     
     
     
     ############ZIP FUNCTION#############
     
     # zip() is used to add the two items index wise or zip them to gether
     
     
     
# l1=[1,4,7,8]
# l2=[-1,-4,-7,-8]
# zip(l1,l2)
# l=[i+j for i ,j in zip(l1,l2)]
# print(l)


#####we can store any built in function in list
# l=[int ,float,type,1,]
# print(l)
# num=int (input("enter the no."))
# sum=0
# n=2
# for i in range(num+1):
#  sum=sum+n
#  n=n*10+2
 

#  print("sum of 2+22+222+2222+22222=",sum)  
# n=(1,2,3,4)
# for i in range(1,5):
#     for j in range(1,5):
#         if i==j or j==i:
#             continue
#         for k in range(1,5):
#             if k==i or k==j:
#                 continue
#             for l in range(1,5):
#                 if l==i or l==j or l==k:
#                     continue
                
#                 print(i,j,k,l)    

# l1="campusx"
# l2="data"
# l3=len(l1)//2
# output=l1[:l3]+l2+l1[l3:]
# print(output)
# Original string
# Original string
# Original string
print('Ben', 25, 'California', sep='--')

