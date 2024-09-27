# st  = {10,85,65,45,72,72,72,72} 
# insert  
# st.add(50) 
# 

# to remove the item from set 10  
# st.pop()  # select random item to remove 
# st.remove()  # to remove specific item and it raised the error if item is not present
# st.discard() # to remove specific item and it not raised the error if item is not present

# st1  = {10,85,65,45,72,72,72,72} 
# st2  = {10,85,62,88}
# print(st1.difference(st2))  # A-b
# print(st2.difference(st1))

# print(st1.intersection(st2) )
# print(st1.union(st2))
# print(st) 
# print(type(st))

# 
# st1.issubset() 
# st1.issuperset() 

# st1  = {10,85,65,45,72,72,72,72} 
# st2  = {10,85,72,2}
# st3  = {10,85,72}
# st4 =  {66,55,44}

# st1.update(st2)
# print(st2.issubset(st1))  # return true if st2 is subset of st1
# print(st1.issuperset(st2))  # return true if st1 is superset of st2
# print(st1.isdisjoint(st4))  # return true when all are unique items in st4

# st1  = {10,85,65,45,72,72,72,72} 
# st1.clear()
# st1.copy()   
 

# duplicates remove 
# ls = [10,20,30,30,50,10,60,10,20,7,77,88,88,99,7,2]
# print(set(ls))  # typecast into set to remove the duplicates 

# print(set(range(1,24)))


# <<<<<<<<<<<<<<<<<<< DICTIONARY   >>>>>>>>>>>>>>>>>>>>>>>
# dt1 =  {'A':25,'B':50,'C':75,'D':100}
# print(dt1)
# print(dt1.keys())   # to extract only keys from the dictionary 
# print(dt1.values())  # to extract only values from  the dictonary 

# print(type(dt1))

# accessing, insert, update , deletion 
# dt1 =  {'A':25,'B':50,'C':75,'D':100}

# print(dt1['D'])  # accessing 
# dt1['D'] = 200   # to update the value of any particular key 
# dt1['E'] = 200   # to insert the item into dictionary 
# print(dt1["Bl"])
# print(dt1.get('Bl','not find'))
# dt1.clear()  
# dt1.copy()  

# dt1 =  {'A':25,'B':50,'C':75,'D':100}
# dt2 = {'E':200,'F':300}

# print(dt1.pop("B"))  # pass tha key of that pair 
# dt1.popitem() # last pair
# print(dt1)
# dt1.update(dt2)
# print(dt1)
# ls = ['A','B','C','D','E']
# print(dict.fromkeys(ls,10))

# ls = list(range(1,25))
# print(dict.fromkeys(ls,"upflairs"))


# dt1 =  {'A':25,'B':50,'C':75,'D':100}
# # dt1.setdefault()   #  home work
# output = [('A', 25), ('B', 50), ('C', 75), ('D', 100)]
# print(dict(output))



