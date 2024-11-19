###Dictionary is used to store the pair of words as it is called map and assocaitive array 

# it is mutable
#it has no indexing 
#no duplicate items
#syntax d={}... it has same brackets like sets




##############   DICCTIOARY################

# Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.

# In some languages it is known as map or assosiative arrays.

# dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }

# Characterstics:

# Mutable
# Indexing has no meaning
# keys can't be duplicated
# keys can't be mutable items
# d={
#     'name':'saram',
#     'class':'issb',
#     'clg':'fic',
#     'school':{
#         'date of pass':2022,
#         'date of pass 10':2021,
#         'live in':'pakistans',
#         'time square':'gmt +5',
        
        
        
#     }  
# }
# print(d)


# as we ca print the sequence like we write upper format 'name':'saram'
# d=dict([(1,2),(3,4)])
# print(d)   #prit like above json format we use tuple within list


#immutavble items are not allowed in dict
   
   
   # we can access the specific item in dict as:
   #sytax d[] this is used to access the item
# d={'name':'saram','gender':'male'}
# print(d['gender'])
# # or secod we use get ()
# print(d.get("name"))

# add item i the dict
#syntax  d['name']='saram'
# d={'name':'saram'}
# print((d))
# d['gender ']='male'
# print(d) from this we can add item into the dict

#some function of dict
#pop is used to delted the item by passing the name we want to deleted
#pop item is used to delted the specfici
#del i used to del specific ad all
#clear is used to clear whole thig

# s={'name':"rahu",'sub':'comp','subj':{
#    'ds':33,
#    'cs':22,
# }}

# we can edi or update the exsisting pair of keys
# s['subj']['ds']=35
# print(s)
# print(s)
# s.pop('name')
# print(s)
# s['subj']['vs']=21 # adding item syntax d[][]=any string or number u want to add
# print(s)
# print(s['subj']['vs'])
# del s['sub']
# print(s)



###########OPERATION ON DICT------------->

#membership op works on keys not on value dennote by in or not in
# d={'name':'sar'}
# print(d)
# print('name'in d)

# loops
# d={"vel":'ball',"gen":"11"}
# for i in d:
#    print(i,":",d[i]) # first it will print keys and then we add dic[i] to prit values

# some more func of dict
#len
#max
#min
#sorted which display output in list 


#some more imp and useful func
#items 
#keys
#valuse

# d={'name':'saram','year':2005,'date':24}
# print(d.items())
# print(sorted(d.keys()))
# print(d.values())

# update func is used to update the firts dict to second like\
# d={1:3,3:4,5:6}
# d2={5:8}
# d.update(d2)
# print(d)


###dict comprehsnins
#{key:values for var in iterable }

# v={i:i**2 for i in range(1,11)}
# print(v)

#we can aslo make a new dict from the existing dict this we can done by 

# d={"shakrial":11,"islama":333,"noora":123}

# print(d.items())

# d2={i:j*0.12 for (i,j) in d.items()}
# print(d2)


# d4={'name':'saram','age':'22'}
# for i in d4:
#    print(i,dict[i])


#how to use zip in dict comprehsnion 


# d1={"mon","tues","wedn","thurs","fri"}
# d2={30,20,13,14,15}
# d3={i:j for (i,j)in zip(d1,d2)}
# print((d3))


# d={1:'mon',2:"tues"}
# d2={i:j for (i,j) in d.values() }
# print(d2)

# d={"lap":0,"charger":2}
# d2={i:j for (i,j) in d.items() if j>0}
# print(d2) ? start the loop to use the upper one as i and j adn then amek a condition


# d={i:{j:i*j for j in range(1,11)}for i in range(2,5)}
# print(d) use to print table 
# test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]






