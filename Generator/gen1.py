def myGen(n):
    value=0
    while value<n:
        yield value
        value+=1
        
for i in myGen(8):
    print(i)
    