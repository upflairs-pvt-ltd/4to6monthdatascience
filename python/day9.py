# ls = [25,45,63,96,85,75]

# for i in range(len(ls)):
    # print(f"Position : {len(ls)-i-1}  ==>  {ls[len(ls)-i-1]}   position : {i} ==> {ls[i]}")

# <<< while >>>> 
# i = 0 
# while i <= 5:
    # print(6-i-1)
    # i += 1 


# i  = 5
# while i >= 0: 
#     print(i) 
#     i -= 1


# ls = [25,45,63,96,85,75,96]
# target = 96
# for i in range(len(ls)): 
    # if ls[i] == target:
        # print(f"your target item {target} is present at this location {i}")


ls = [25,45,63,96,85,75,96]
total_sum = 0 
# print(sum(ls)) 
for item in ls:
    # total_sum = total_sum + item 
    total_sum += item 
print(total_sum)
    




n = 5

# Print the pattern
for i in range(1, n + 1):
    print("*" * i)

# *
# **
# ***
# ****
# *****

# Number of rows
n = 5

# Print the pattern
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

    # *
#    **
#   ***
#  ****
# *****

###
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()


####



for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()


