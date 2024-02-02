# def print_name():
#     def print_sirName():
#         print("Thorat")
#     print('Sanchit')
#     print_sirName()

# print_name()



# s=True
# print(type(s))

# age=input("Enter the age:")
# new_age=float(age)+2
# print(new_age)
# Get a space-separated list from the user
# user_input = input("Enter a space-separated list of values: ")

# Split the input string into a list and convert each element to an integer
# user_list = list(map(int, user_input.split()))

# Display the resulting list
# print("List of integers from user input:", user_list)

# name="Sanchit"
# name.translate

name = "Sanchit"

# Example translation table (mapping 'S' to 'X' and 'a' to 'A')
translation_table = str.maketrans({'S': 's', 'a': 'A'})

# Using translate with the translation table
new_name = name.translate(translation_table)

print("Original name:", name)
print("Translated name:", new_name)

