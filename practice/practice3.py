'''slicing: is the extrating certain elements from the list'''
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#index     0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#reverse  10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# list[start:end:step]
print(my_list[0])
print(my_list[-10])
print(my_list[0:6])
print(my_list[-7:-1])
print(my_list[-1:-10])
print(my_list[-1:-10:-2])
print(my_list[::])
print(my_list[::-1])

'''sorting lists,tuples,objects'''

li = [9,5,4,2,1,6,8,7,3]
s_li =  sorted(li)
print("sorted list",s_li)
li.sort()
print("original list:",li)

