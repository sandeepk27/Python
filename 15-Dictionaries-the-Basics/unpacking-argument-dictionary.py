# Define a function
def introduce(name, age, city):
    print(f"My name is {name}, I am {age} years old, and I live in {city}.")

# Create a dictionary
person_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Unpack the dictionary using ** and pass it to the function
introduce(**person_info)


# handling extra keys

# Function with **kwargs
def introduce_with_kwargs(name, **kwargs):
    print(f"My name is {name}.")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

# Dictionary with additional keys
extended_info = {
    "name": "Bob",
    "age": 35,
    "city": "Los Angeles",
    "hobby": "Photography"
}

# Call the function
introduce_with_kwargs(**extended_info)
