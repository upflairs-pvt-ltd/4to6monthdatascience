# # 1. define  
# # 2. calling   


# # 1. defining function 
# def average_calculater(input_ls):
#     total_sum = 0 
#     count = 0 
#     for item in input_ls: 
#         total_sum += item 
#         count += 1 
#     print("your average is : ", total_sum/count)
# # 2. # calling function 


# ls = [52,63,52,85,96,74]

# average_calculater(input_ls=ls)
# ls2 = [852,963,456,75,62,41,85,66,55,44,88,99,25]
# average_calculater(input_ls=ls2)
# ls3 = [852,963,456,75,62,41]
# average_calculater(input_ls=ls3)



# # ls2  = [96,78,95,45,25,55,66,33]




## add two 
# def add_two(num1, num2):
    # result = num1 + num2 
    # print("Your sum is : ", result) 
    # return result 

# n1 = 25 
# n2 = 25 
# add_two(num2=35,num1=n1) 
# add_two(n1,n2)
# add_two(30,25)
# st = "hello world"
# print(st)
# output = add_two(40,25)
# print("my sum is : ",output)


# test = 100
# def multiply():
#     num1 = 10 
#     num2 = 5 
#     result = num1 * num2 
#     return result 

# ouput = multiply()
# print(ouput)

# print(multiply())
# print(test)
# print(num1)

x = 25 
def test():
    global x 
    x = 50
    print(x) 
test()
print(x)

