name="Sanchit thorat"
print(name[::-1])
print(name[::-1])
print(name[0:3])
# print("nagic ",name[0:14])
# print("nagic ",name[0:6])


length=len(name)
print(length)

# print(name[:length])







# In Python slicing, when you use a step value of -1, such as [::-1], it means that you want to iterate through the sequence (string, list, etc.) in reverse order.

# In the specific case of name[::-1]:

# The first colon (:) before the second colon (:) represents the start index. Since it is not specified (::-1), it defaults to the end of the sequence.

# The second colon (:) separates the start index from the end index.

# The third part (-1) after the second colon is the step value. In this case, the step is -1, indicating that you want to traverse the sequence backward.

# So, name[::-1] reverses the string "Sanchit thorat". The -1 step makes it iterate through the string in reverse order, effectively creating the reversed string. The output would be:

# Copy code
# taroht tihcnaS