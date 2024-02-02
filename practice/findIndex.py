age=[]
n=int(input("Enter the totla number of ages:"))
for i in range(1,n+1):
    age.append(int(input("Enter the age number {}:".format(i))))
middle=[]
young=[]
for data in age:
    if(data>20):
        middle.append(data)
    else:
        young.append(data)

print("The middle group people is ",len(middle), middle)
print("The young group people is ", len(young),young)