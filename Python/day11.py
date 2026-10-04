#List --> Ordered, mutable collection of elements 
#Tuple --> Ordered, immutable collection of elements
#Set --> Unordered, mutable collection of unique elements
#Dictionary --> Unordered, mutable collection of key-value pairs



a = [1, 2, 3, 4, 5] #List

#List methods
a.append(6) #Adds an element to the end of the list
print(a) #Output: [1, 2, 3, 4, 5, 6]

a.append([7, 8, 9]) #Adds a list as a single element to the end of the list
print(a) #Output: [1, 2, 3, 4, 5, 6, [7, 8, 9]]

a.extend([7, 8, 9]) #Adds multiple elements to the end of the list
print(a) #Output: [1, 2, 3, 4, 5, 6, [7, 8, 9], 7, 8, 9]

a.extend((7, 8, 9)) #Adds multiple elements to the end of the list
print(a) #Output: [1, 2, 3, 4, 5, 6, [7, 8, 9], 7, 8, 9, 7, 8, 9]

a.extend({7, 8, 9}) #Adds multiple elements to the end of the list
print(a) #Output: [1, 2, 3, 4, 5, 6, [7, 8, 9], 7, 8, 9, 7, 8, 9, 7, 8, 9]

a.extend({"a": 1, "b": 2, "c": 3}) #Adds multiple elements to the end of the list
print(a) #Output: [1, 2, 3, 4, 5, 6, [7, 8, 9], 7, 8, 9, 7, 8, 9, 7, 8, 9, {'a': 1, 'b': 2, 'c': 3}]

a.extend(("a", "b", "c")) #Adds multiple elements to the end of the list
print(a) #Output: [1, 2, 3, 4, 5, 6, [7, 8, 9], 7, 8, 9, 7, 8, 9, 7, 8, 9, {'a': 1, 'b': 2, 'c': 3}, ('a', 'b', 'c')]

a.insert(2, 10) #Inserts an element at a specific index
print(a) #Output: [1, 2, 10, 3, 4, 5, 6, [7, 8, 9], 7, 8, 9, 7, 8, 9, 7, 8, 9, {'a': 1, 'b': 2, 'c': 3}, ('a', 'b', 'c')]

a.insert(2, [10, 11, 12]) #Inserts a list as a single element at a specific index
print(a) #Output: [1, 2, [10, 11, 12], 10, 3, 4, 5, 6, [7, 8, 9], 7, 8, 9, 7, 8, 9, 7, 8, 9, {'a': 1, 'b': 2, 'c': 3}, ('a', 'b', 'c')]

a.pop() #Removes and returns the last element of the list
print(a) #Output: [1, 2, [10, 11, 12], 10, 3, 4, 5, 6, [7, 8, 9], 7, 8, 9, 7, 8, 9, 7, 8, 9, {'a': 1, 'b': 2, 'c': 3}, ('a', 'b', 'c')]

a.pop(2) #Removes and returns the element at a specific index
print(a) #Output: [1, 2, 10, 3, 4, 5, 6, [7, 8, 9], 7, 8, 9, 7, 8, 9, 7, 8, 9, {'a': 1, 'b': 2, 'c': 3}, ('a', 'b', 'c')]

a.remove(3) #Removes the first occurrence of an element
print(a) #Output: [1, 2, 10, 4, 5, 6, [7, 8, 9], 7, 8, 9, 7, 8, 9, 7, 8, 9, {'a': 1, 'b': 2, 'c': 3}, ('a', 'b', 'c')]

a.remove([3, 4]) #Removes the first occurrence of an element
print(a) #Output: [1, 2, 10, 4, 5, 6, [7, 8, 9], 7, 8, 9, 7, 8, 9, 7, 8, 9, {'a': 1, 'b': 2, 'c': 3}, ('a', 'b', 'c')]

a.clear() #Removes all elements from the list
print(a) #Output: []

a.index(10) #Returns the index of the first occurrence of an element
print(a) #Output: 2
print(a.index(10, 3)) #Returns the index of the first occurrence of an element starting from a specific index
print(a.index("a")) #Returns the index of the first occurrence of an element

print(a.count(1)) #Returns the number of occurrences of an element
print(a.count(10)) #Returns the number of occurrences of an element

print(a.sort()) #Sorts the list in ascending order
print(a.sort(reverse=True)) #Sorts the list in descending order

a.copy() #Returns a shallow copy of the list
print(a) #Output: [1, 2, 10, 4, 5, 6, [7, 8, 9], 7, 8, 9, 7, 8, 9, 7, 8, 9, {'a': 1, 'b': 2, 'c': 3}, ('a', 'b', 'c')]

