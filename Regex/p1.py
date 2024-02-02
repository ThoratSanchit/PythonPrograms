import re

emp = "Myt My phone number is 8208170915. Another one is 9822995836. John Doe: +9834567890 Jane Smith: +9876543210 Bob Johnson: +9822334455 Alice Williams: +9288776655"

numbers = re.findall(r"\b(?:\+?1[-.\s]?)?(?:\(?([2-9][0-8][0-9])\)?[-.\s]?)?([2-9][0-9]{2})[-.\s]?([0-9]{4})\b", emp)

for number in numbers:
    # print(number[0] + number[1] + number[2])  # Corrected to concatenate as strings
    # print("".join(numbers))
     print("".join(map(str, number)))

capt = re.findall(r"[A-Z]+", emp)

pattern = "Myt"
ssearch = re.search(pattern, emp)
print(ssearch)
