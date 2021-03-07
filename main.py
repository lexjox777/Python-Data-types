'''
# Text Type(string)

# '''
# s='This is a single line string'
# print(s)
# print(type(s))

#===================

# s='''This is a multiple 
# string example'''
# print(s)

# ===============
# find a character by index
# s= 'string sample'
# print(s[5])

# ============
# immutable (the string value cant be changed)
# s= 'string sample'
# s[2]='o'
# print(s)


# ============
'''
Numeric Type(Integer, Float, Complex)
'''
# integer
# x=1234563647892367
# print(type(x))


#float is accurate up to 15-16 decimal places
# x=0.123456256738492010
# print(type(x))
# print(x)


# complex

# x=1+2j
# print(type(x))

'''
Sequence Type (list, Tuple, Range)
'''

# list
# list []
# x=[10, 2.5, 'hello']
# print(x[0])
# print(x[1])
# print(x[2])


# list is  mutable ( this can be change )
# x=[10, 2.5, 'hello']
# x[2]='python'
# print (x)

# Tuple ()
# tuple =()
# tuple=('cat',[4,2,1],(2,3,4)
# print(type(tuple))
# print(tuple)

# note tuple use comma to make it valid, without comma makes it a string
# tuple1=('hello',)
# tuple2=('hello')
# print(type(tuple1))
# print(type(tuple2))
# print(tuple1)
# print(tuple2)

# #  Tuple is immutable
# tuple=('cat',[4,2,1],(2,3,4)
# tuple[2]=10
# print(tuple)


# ==========================
# Range
# x= range(10)
# for n in x:
#  print(n)


'''
Mapping Type(Dictionary)
# '''
# # dict={}
# # print(type(dict))

# #===============
# dict={'name': 'Kingsley','age':35}
# # print(dict['age'])
# # print(dict['name'])

# # another way of using dict
# print(dict.get('name'))

# # dict is mutable i.e values can be changed Thus;

# dict['age']=26
# print(dict)

'''
Set Types
'''
# set has single values

# set={1,2,3}
# print(type(set))
# #empty set having set ={} is an empty dict instead use set=set()
# set=set()

#==============
# set can have a mixed data types that are immutable
# set= {3,2, 'hi',(1,2,3)}
# print(type(set))
# # set does not support indexing
# print(set[0])

#=================
# no duplicate items in set
# set={3,2,'hi',(1,2,3),'hi'}
# print(set)

# ===============
# we cannot have mutable[list] in a set
# set={3,2,'hi',(1,2,3),[1,2,3]}
# print(set)

'''
Boolean Type(True or False)
'''

print(type(True))

# boolean as numbers
print(True==1)
print(False==0)

# boolean as logic
print(True+True)

# 'Not' boolean  operator
print(not True)
print(not False)

# 'And' boolean operator

print(True and False)
print(False and True)
print(True and True)

# 'or' boolean operator
print(True or True)
print(True or False)
print(False or False)
