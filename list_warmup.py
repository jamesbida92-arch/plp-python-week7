# list_warmup.py

fruits = ["apple", "banana", "orange", "mango"]

# Print the first and last items using indexes
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add a fifth fruit
fruits.append("pineapple")
print("After append:", fruits)

# Remove one fruit
fruits.remove("banana")
print("After remove:", fruits)

# Print the number of fruits remaining
print("Number of fruits:", len(fruits))