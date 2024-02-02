# 2) write the program to print all the number from 0 t0 6, but not print 3 and 6
for i in range(1,7):
    if i==3:
        continue
    elif i==6:
        continue
    print(i)