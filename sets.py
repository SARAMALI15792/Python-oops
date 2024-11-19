#sets are denoted by {}
#unoredersed do not follow the sequence 
#no duplicate is allowed in sets
#sets are mutable but we cannot add sets within sets 
#it is homogenous as well as hetrogenous it support single and all datatype but if it has
#duplicate item are not print again ..like {1,true} it print 1 only as true refer in python as 1 and false refer in python 0


###########   SETS   ##########
# A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

# However, a set itself is mutable. We can add or remove items from it.

# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

# Characterstics:

# Unordered
# Mutable
# No Duplicates
# Can't contain mutable data types


#creting sets
# s={1,2,3,"hellow",True}
# print(type(s))
# print(s)

 #---------------->indexing and slicing---------<<<<
#-----> no indexing or slicing is work in sets as becasue sets have unordered and cannot have duplicate

#############   func of sets
#add can add only one item at the time and update like append and extend
# s={"saram ","ali"}
# s.add("saleem")
# print(s)

#update can add multiple itms at the same time
#syntax s.update([])
# s={1,2,3,4,55}
# s.update([56,67,6,8])
# print(s)

#some more func in sets{}
#del is used to delted the sets
#remove is used to remove a single items from the progrm if we remove out of range it throws error
#discard is used to remove similar like remove but dom not throw error while we write out of range items
#pop is randomaly delete any item from the sets
#clear is used to clear the whole program in programming

# some example of these are
# s={1,2,3,4}
# s.discard(4)
# print(s)
# s.remove(3)
# print (s)
# s.pop()
# print(s)


#----------> some operations on sets------->
#union op(|) is used to print or merge the two sets
#interrsection op (&) is used to print the common items
#difference op(-)it is to drop the common and print the items which is not present in other sets
#symmetric difference op(^)is used to leave the commons items and print the rest of items
#membership (in or not in) is used to tell the presence or not presence of item in eachother sets
#loops are also used on sets


#####now we have seen example ###
# s1={1,2,3,4}
# s2={4,5,6,7,8}
# print(s1 | s2) # this is union function
# print(s1 & s2) # this is intersection op
# print(s1 - s2) # this is differnece which drop common and then write rest of thses of one set 
# print((s2-s1))# this will also reapt the same process
# print(s1 ^ s2)# this drops common item and print rest of all intem in set 



###---------->> also use in spell words
# s={1,2,3}
# s2={4,3,5,7}
# s.union(s2)
# print(s)
# s.update(s2)
# print(s)
# s.intersection(s2)
# print(s)
# s.intersection_update(s2)
# print(s)
# s.difference(s2)
# print(s)
# s.difference_update(s2)
# print(s)
           
# s.symmetric_difference(s2)
# print(s)
# s.symmetric_difference_update(s2)
# print(s)                        

#u  can also used this spell operation also in sets
#isdisjoint is used to check no common items in sets
#issubset is used to chk the the common items of other sets
#issupersetis super of another

# s={1,2,3,4}
# s2={3,4,5}
# print(s.issupers(s2))

#########       FROZEN SET  #########
# it is immutable of python version
#as u can pass tuple ,set or list in frozen sets 
#it works on all read operations sets like union ,intersection, and etc
#as it work on 2d sets and 3d also work
#syntax--- frozenset(pass any tuple or..)

# w=frozenset({1,2,3,4,frozenset({1,2,3,4})})
# print(w)


###### set comprehsension also work as same in list and sets:
# l={count for count in range(1,10) if count >5 if count <9}
# print(sorted(l))

# username=input("enter your name: ")
# password=input("enter your password")
# print("your user name is {} and your password is {}".format(username,password))