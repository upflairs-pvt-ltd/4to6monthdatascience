## find out average of all the even number 
# ls = [52,63,45,85,62,33,14,52,63,96,85,45,75,6,5]
# total_sum = 0 
# count = 0
# for item in ls:
#     if item % 2 == 0:   # True 
#         # total_sum = total_sum + item 
#         total_sum += item 
#         count += 1 

# print(total_sum/count)





# ls = [52,63,45,85,62,33,14,52,63,96,45,85,96,25,78,251,85,45,75,6,5]
# total_sum = 0
# count = 0
# for item in ls:
    ## logical operator if condition1 and condition2 :
#     if (item > 70 and item < 90) and item % 2 == 0:
#         print(item)
#         total_sum = total_sum + item
#         count += 1
# avg = (total_sum/count)
# print(avg)


st = "upflairs pvt ltd jaipur rajasthan"
dt = {}
for char in st:
    # print(f" {char}  ===>  {st.count(char)}") 
    dt[char]  = st.count(char)
print(dt)


 

