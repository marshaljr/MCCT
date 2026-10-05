# Loop in List

# list1 = ["Ram", "Shyam", "Mohan", "Sohan"]
# for i in list1:
#     print(i) #Output: Ram Shyam Mohan Sohan


# list2 = [80,72,98,90, 32]
# for marks in list2:
#     if marks >= 40:
#         print("Pass", marks) #Output: Pass 80 Pass 72 Pass 98 Pass 90
#     else:
#         print("Fail", marks) #Output: Fail 32


# list3 = [10, 12, 15, 20, 25, 30]
# for i in list3:
#     if i % 2 == 0:
#         print("Even", i) #Output: Even 10 Even 12 Even 20 Even 30
#     else:
#         print("Odd", i) #Output: Odd 15 Odd 25


# list4 = [1,2,3,4,5,6,7,8,9,10]
# for i in list4:
#     if i > 1:
#         for j in range(2, i):
#             if (i % j) == 0:
#                 break
#             else:
#                 print("Prime", i) #Output: Prime 3 Prime 5 Prime 7 Prime 9
#             break



# list5 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for i in list5:
#     if i > 10:
#         print("Greater than 10", i)



# list6 = [10,20,30,4,5,6,7,8,9,22,25]
# i=0
# while i < len(list6):
#     print(list6[i]) #Output: 10 20 30 4
#     i += 1

# i=0
# while i < len(list6):
#     if list6[i] > len(list6):
#         print("Greater than 10", list6[i]) #Output: Greater than 10 20 Greater than 10 30
#     i += 1





# #Tuple --> Ordered, immutable collection of elements
# tuple1 = ("Ram", "Shyam", "Mohan", "Sohan")
# # print(tuple1[-1]) 
# # print(tuple1[0:3])
# # print(tuple1.index("Mohan"))
# # print(tuple1.count("Ram"))

# tuple1 = list(tuple1)

# tuple1.append("Ramesh")
# tuple1 = tuple(tuple1)
# print(type(tuple1)) #Output: <class 'tuple'>
# print(tuple1) #Output: ('Ram', 'Shyam', 'Mohan', 'Sohan', 'Ramesh')





#Set --> Unordered, mutable collection of unique elements

# set1 = {10, 50, 10, 20, 30, 40, 50, 40, 50}
# print(set1) 

# set1.add(6)
# print(set1) #Output: {10, 20, 30, 40, 50, 6}

# set1.copy()
# print(set1) #Output: {10, 20, 30, 40, 50, 6}

# set1.update([7, 8, 9])
# print(set1) #Output: {10, 20, 30, 40, 50, 6, 7, 8, 9}

# # set1.remove(3)
# # print(set1) #Output: {10, 20, 40, 50, 6, 7, 8, 9}

# set1.discard(4)
# print(set1) #Output: {10, 20, 50, 6, 7, 8, 9}

# set1.pop()
# print(set1) #Output: {20, 50, 6, 7, 8, 9}

# set1.clear()
# print(set1) #Output: set()


set2 = {1, 2, 3, 4, 5}
set3 = {4, 5, 6, 7, 8}

print(set2 | set3) #Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set2.union(set3)) #Output: {1, 2, 3, 4, 5, 6, 7, 8}

