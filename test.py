# Basic use of print()
print("Hello, World!")
print("This is a simple message.")

# print() with multiple arguments
print("Name:", "Alice", "Age:", 25)

# print() with formatted strings (f-strings)
name = "Bob"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Function that uses print()
def greet(person):
    print(f"Hello, {person}! Welcome!")

# Function that calculates and prints a result
def calculate_sum(a, b):
    total = a + b
    print(f"The sum of {a} and {b} is {total}.")

# Function that prints a list of items
def print_items(my_list):
    print("Here are the items:")
    for item in my_list:
        print(f"- {item}")

# Calling the functions
greet("Charlie")
calculate_sum(10, 15)
print_items(["Python", "Java", "JavaScript"])