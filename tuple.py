#tuple   is denoted by ()    
#it is immutable cannot be changed 
#various ways to create it 
# it is hetrogenous 
#it is similar to list as liost is mutable and tuple and string is not mutable
#1 for single t=33  print(t,)   this is syntax to print
# this fro single 
###########
####tuple##########
# A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

# In short, a tuple is an immutable list. A tuple can not be changed in any way once it is created.

# Characterstics

# Ordered
# Unchangeble
# Allows duplicate

################

# t=(33,)
# print(type(t))  used to print single item 

# t=("saram",33.33,True,)
# print(t)  this is hetro genous way to create a tuple 


#########indexind and slicing in tuple###########
# t=(12,34,34,(1,4))
# print(t[-1][0])
#it is same as in previous string and list

#editing 
#delteing the signle tuple item does not work as it works only on del full tuple
#adding would aslo not work as it does not suppport in tuple
#changing or replacing would not be work in tuple 

#######OPERATION ON TUPLE###########|
#+ and *
#membership
#loop
# t=(1,2.3,5)
# t1=(6,70,0)
# print(sorted(t+t1)*3)

# t=(0,3,45,222,455)
# for i in t:
#     print(i)


######FUNCTION ON TUPLE ######
#len,sum,min,max,sorted (when use sorted it will print it in list tuple convert to list)


# t=(22,33,0,1,2)
# print(sum(t))
# print(max(t))
# print(min(t))
# print(sorted(t))
# print(sorted(t,reverse=True))


#count ,index
# t=(1,2.3,5)
# print(t.count(2.3))
# print(t.index(5))

##########Tuple unpacking as it has special syntax
# a,b,*others=(1,2,3)
# print(a,b)
# print (others)# this is because it as we have two variable to declare on the other side it has many

#so we can mange this by a,b,*others(as *others will store the extra items and display it in list
# 
# )

######SWAPING A NUMBERS IN  PYTHON### as in otherr language it require third varible to swap
# a,b=(2,1)
# print(a,b)
# a,b=b,a
# print(a,b)


#########ZIP  Function #########
#it is used to zip the items and displat it in any format like list and tuple

# z=("saram")
# x=(1,2,3)
# zip(z,x)
# print(tuple(zip(z,x)))
