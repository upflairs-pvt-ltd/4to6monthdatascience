### built-in 
### user-defined 
## return 
## args and kwargs 
## prectise 

### lambda function 
# incr = lambda x:x**2
# print(incr(2))


# addnumber = lambda num1,num2:num1 + num2
# print(addnumber(num1=25,num2=25))

# def testing1():
#     print('heyy testing1')

# def testing2():
#     print('hey testing2')

# def testing3(fun1,fun2):
#     fun1()
#     fun2()


# testing3(fun1=testing1,fun2=testing2)


## map()

# ls = [2,3,4,5,6,7,8,9]
# for item in ls:
#     print(item**2)

# def square_finder(x):
    # return x**2

# ls = [2,3,4,5,6,7,8,9]   
# output  =  list(map(square_finder,ls))
# print(output)





# ls = [2,3,4,5,6,7,8,9]   
# output  =  list(map(lambda x : x**2,ls))
# print(output)

# print(square_finder(5))

## <<<<<<<<<<<<, creating yuor own map >>>>>>>>>>>>>>>>>
# def square_finder(x):
#     return x**2


# def my_map(fun,iterable):
#     data = []
#     for item in iterable:
#         data.append(fun(item))
#     return data 


# ls = [2,3,4,5,6,7,8,9]
# print(my_map(fun=square_finder,iterable=ls))




words_ls = ['hello','hyy','how','are','you','education','graduate']
len_character = list(map(len,words_ls))
maximum_length = max(list(map(len,words_ls)))

print(len_character)
print(maximum_length)