# creating empty list
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
item = 10
for i in range(4):
    my_list.append(item)
    item += 10

# check if elements were appended successfully
print(my_list)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)
print(my_list)  # check

# Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])

# Remove the last element from my_list.
my_list.pop()

# Sort my_list in ascending order.
my_list.sort() 

# Find and print the index of the value 30 in my_list.
print(my_list.index(30))

print(my_list)  # final check