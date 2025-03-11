# sample_dict={
#     'physics':82,
#     'maths':65,
#     'history':75
# }
# my_list=[]
# for i in sample_dict.values():
#   my_list.append(i)
# # print(f"the minimum value in the list is {min(my_list)}")
# print(min(my_list))

tuple3=(11,22,33,44,55,66)
tuple4=[]
print(tuple4)
tuple5=list(tuple3)
tuple4.append(tuple3.pop(3))
tuple4.append(tuple5.pop(4))
print(tuple(tuple5))
print(tuple(tuple4))

