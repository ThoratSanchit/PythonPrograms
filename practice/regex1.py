import re

# Search for a pattern in a string
text = "The price of the product is $20.50"
pattern = r'\$\d+\.\d{2}'  # Matches a dollar sign followed by digits and a decimal point
match = re.search(pattern, text)

if match:
    print(f"Found: {match.group()}")
else:
    print("Pattern not found")

# Using re.findall to find all occurrences of a pattern
text = "The colors are red, green, and blue ."
colors_pattern = r'\b\w+\b'  # Matches whole words
all_colors = re.findall(colors_pattern, text)
print(all_colors)



text="jnh hbhbh bhbhb"
# c=re.search('\s',text)
c=re.search('LANG',text)

print("The white space",c)