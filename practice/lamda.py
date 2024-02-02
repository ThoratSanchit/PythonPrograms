x=map(lambda  x:x*3, range(10))
print(x)


listNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


odd = list(filter(lambda x: x % 2 != 0, listNum))


even = list(filter(lambda x: x % 2 == 0, listNum))


print("Original list:", listNum)
print("Odd list:", odd)
print("Even list:", even)

square=list(map(lambda x:x**x,listNum) );
print("Square of a every number ",square)

qube=list(map(lambda x:x*x*x,listNum))
print("Qube ",qube)

