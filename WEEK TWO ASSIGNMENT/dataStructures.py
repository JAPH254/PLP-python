# my empty list called my_list
my_list = []

# Append elements 10, 20, 30, 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Print the list after appending elements
print("List after appending:", my_list)

# Insert the value 15 at the second position
my_list.insert(1, 15)

# Print the list after insertion
print("List after insertion:", my_list)

# Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Print the list after extending
print("List after extending:", my_list)

# Remove the last element from my_list
my_list.pop()

# Print the list after removing the last element
print("List after removing last element:", my_list)

# Sort my_list in ascending order
my_list.sort()

# Print the sorted list
print("List after sorting:", my_list)

# Find the index of the value 30 in my_list
index_of_30 = my_list.index(30)

# Print the index of 30
print("Index of 30 in the list:", index_of_30)
