# Creating a nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Accessing elements
print(nested_list[0])
print(nested_list[0][1])    

# Iterating through a nested list
for sublist in nested_list:
    for item in sublist:
        print(item, end=" ")  
        
# basic nested list comprehension
# Creating a 3x3 matrix
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


# Flattening using list comprehension
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

