a=[]
n=int(input("Enter the number of elements:"))

for i in range(1,n+1):
    a.append(int(input("Enter the elements {} :".format(i))))

oddList=list(filter(lambda x:x%2!=0,a))
evenList=list(filter(lambda x:x%2==0,a))
print("The odd list", oddList)
print("The even list", evenList)