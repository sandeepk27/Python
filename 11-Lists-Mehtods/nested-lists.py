# A nested list representing a matrix
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a nested list
print("Element at row 1, column 2:", nested_list[0][1])

# Iterating through a nested list
print("Iterating through the nested list:")
for row in nested_list:
    for element in row:
        print(element, end=" ")
    print()

# Modifying an element
nested_list[1][1] = 50
print("Modified Nested List:", nested_list)

# Adding a new sublist
nested_list.append([10, 11, 12])
print("After Adding a Sublist:", nested_list)

# Removing a sublist
nested_list.pop(0)  # Removes the first sublist
print("After Removing a Sublist:", nested_list)

# List comprehension to flatten a nested list
flattened_list = [element for row in nested_list for element in row]
print("Flattened List:", flattened_list)

# Example of creating a nested list dynamically
nested_list_dynamic = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Dynamically Created Nested List:", nested_list_dynamic)
