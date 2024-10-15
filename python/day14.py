#######  ZIP()
# ls1 = ["A",'B','C','D','E']
# ls2 = [10,20,30,40,50]
# ls3 = [0.1,0.2,0.3,0.4,0.5]
# output = list(zip(ls1,ls2))
# print(output)

# output2 = dict(output)
# print(output2)
# for item in zip(ls1,ls2):
#     print(item)


### unzip  
# a , b = list(zip(*output))
# print(list(a))
# print(list(b))



## zip()
ls1 = [25,63,45,68,52]
ls2 = [25,42,36,25,44]
ls3 = [54,63,96,85,45]
ls4 = [54,63,96,85,45]


for item in zip(ls1,ls2):
    print(max(item))
## unzip()