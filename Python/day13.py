# set1 = {10,20,30,40,50}
# set2 = {40,50,60,70,80}

# print(set1 & set2)  # Intersection of set1 and set2
# print(set1 - set2)  # Difference of set1 and set2


# list1 = [10,10,20,30,30]

#FIND DUPLICATE FROM LIST1 AND STORE IT IN SET
# duplicates = set()
# for item in list1:
#     if list1.count(item) > 1:
#         duplicates.add(item)
# print(duplicates)  # Output: {10, 30}

#REMOVE DUPLICATE FROM LIST1 AND CONVERT IT IN SET
# list1 = set(list1)
# print(list1)  # Output: [10, 20, 30]




#Dictionary
# student1 = {
#     "name": "John",
#     "age": 20,
#     "courses": ["Math", "Science"]
# }

# print(student1["name"])  # Output: John
# student1["name"] = "Ironman"  # Update the name
# print(student1["name"])  # Output: Ironman

# student1["grade"] = "A"  # Add a new key-value pair
# print(student1)  # Output: {'name': 'Ironman', 'age': 20, 'courses': ['Math', 'Science'], 'grade': 'A'}

# del student1["grade"]  # Remove the grade key-value pair
# print(student1)  # Output: {'name': 'Ironman', 'age': 20, 'courses': ['Math', 'Science']}



# 1. Get the value of a key using the get() method

# print(student1.get("name"))  # Output: Ironman
# print(student1.get("grade", "Not Found"))  # Output: Not Found (default value if key doesn't exist)


# # 2. Keys and Values
# print(student1.keys())  # Output: dict_keys(['name', 'age', 'courses'])
# print(student1.values())  # Output: dict_values(['Ironman', 20, ['Math', 'Science']])
# print(student1.items())  # Output: dict_items([('name', 'Ironman'), ('age', 20), ('courses', ['Math', 'Science'])

# for i in student1.keys():
#     print(i)  # Output: ('name', 'Ironman'), ('age', 20), ('courses', ['Math', 'Science'])

# for i in student1.values():
#     print(i)  # Output: Ironman, 20, ['Math', 'Science']

# for i in student1.items():
#     print(i)  # Output: ('name', 'Ironman'), ('age', 20), ('courses', ['Math', 'Science'])

# for i, j in student1.items():
#     print(i, j)  # Output: name Ironman, age 20, courses ['Math', 'Science']




# Updates

# names = {
#     "name1": "John",
#     "name2": "Jane",
#     "name3": "Alice"
# }

# names.update({"name4": "Bob"})  # Add a new key-value pair
# print(names)  # Output: {'name1': 'John', 'name2': 'Jane', 'name3': 'Alice', 'name4': 'Bob'}


# # pop & popitem

# names.pop("name2")  # Remove the key-value pair with key "name2"
# print(names)  # Output: {'name1': 'John', 'name3': 'Alice', 'name4': 'Bob'}

# # popitem() removes and returns an arbitrary key-value pair from the dictionary
# item = names.popitem()
# print(item)  # Output: ('name4', 'Bob')
# print(names)  # Output: {'name1': 'John', 'name3': 'Alice'}


# names.clear()  # Remove all key-value pairs from the dictionary
# print(names)  # Output: {}



# students = {
#     "Ram" : 75,
#     "Shyam" : 85,
#     "Mohan" : 90,   
#     "Sooraj" : 80
# }

# for name, marks in students.items():
#     if marks >= 80:
#         print(f"{name} has scored {marks} marks and has passed the exam.")
#     else:
#         print(f"{name} has scored {marks} marks and has failed the exam.")


# total = 0
# for marks in students.values():
#     total += marks
#     avg_mark = total / len(students)
#     print(f"The average marks of the students is: {avg_mark}")
