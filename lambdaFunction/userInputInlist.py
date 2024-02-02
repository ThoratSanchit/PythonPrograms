# Take user input for the number of elements
num_elements = int(input("Enter the number of elements: "))

# Create a list based on user input
user_list = []
for i in range(1, num_elements + 1):
    user_list.append(int(input(f"Enter element {i}: ")))

# Filter even and odd elements using lambda and map
even_elements = list(filter(lambda x: x % 2 == 0, user_list))
odd_elements = list(filter(lambda x: x % 2 != 0, user_list))

# Print the results
print("Original List:", user_list)
print("Even Elements:", even_elements)
print("Odd Elements:", odd_elements)
